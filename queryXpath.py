import os
import json
from lxml import etree
from bs4 import BeautifulSoup
import html

def html_to_text(html_string):
    # Usa BeautifulSoup per eliminare i tag e ottenere il testo
    soup = BeautifulSoup(html_string, 'html.parser')
    
    # Decodifica le entità HTML come &#8220; o &#8209;
    decoded_text = html.unescape(soup.get_text())

    return decoded_text

# Funzione per eseguire una query XPath su un file XML o HTML
def execute_xpath_query(file_path, xpath_query):
    try:
        with open(file_path, 'rb') as f:
            # Parsing del file con lxml
            tree = etree.parse(f)
            
            # Esecuzione della query XPath
            results = tree.xpath(xpath_query)
            
            # Ritorno dei risultati della query
            return results
    except Exception as e:
        print(f"Errore nell'eseguire la query XPath su {file_path}: {e}")
        return None

# Funzione per processare tutti i file HTML nella cartella 'sources' e salvare i risultati in un dizionario
def process_all_html_files():
    folder_path = 'sources'
    extraction_path = 'extractions'  # Cartella per i file JSON

    # Crea la cartella 'extractions' se non esiste
    if not os.path.exists(extraction_path):
        os.makedirs(extraction_path)
    
    # Iterare sui file nella cartella 'sources'
    for file_name in sorted(os.listdir(folder_path)):
        if file_name.endswith('.html'):
            file_path = os.path.join(folder_path, file_name)
            print(f"\nProcessando file: {file_name}")
            print("--------------------------------------------------------------------------------------")

            # Dizionario per memorizzare i risultati delle tabelle di questo file
            file_results = {}

            # 1. Trova tutti gli ID delle tabelle o figure
            table_ids = execute_xpath_query(file_path, '//table/@id')
            if not table_ids:
                print(f"Nessun ID di tabella trovato nel file {file_name}.")
                continue

            processed_ids = set()  # Set per tracciare gli ID già processati

            # Itera su ogni ID trovato
            for table_id in table_ids:
                # Assicurarsi che l'ID non sia stato già processato
                if table_id in processed_ids:
                    continue
                processed_ids.add(table_id)  # Aggiungi l'ID al set di quelli processati

                print(f"Processando ID: {table_id}")

                # 2. Query dinamiche basate sull'ID
                query_figureID = f'//table[@id="{table_id}"]/ancestor::figure/@id'
                figure_id = execute_xpath_query(file_path, query_figureID) or []
                
                query_caption = f'//table[@id="{table_id}"]/ancestor::figure//figcaption/text()'
                query_table = f'//table[@id="{table_id}"]/ancestor::figure//table'
                query_footnotes_id = f'//table[@id="{table_id}"]/ancestor::figure//cite/a/@href'
                
                if(figure_id):
                    query_references = f"//*[substring(@href, string-length(@href) - string-length('#{figure_id[0]}') + 1) = '#{figure_id[0]}']/ancestor::p" 
                else:
                    query_references = f"//*[substring(@href, string-length(@href) - string-length('#{figure_id}') + 1) = '#{figure_id}']/ancestor::p" 

                footnote_ids = execute_xpath_query(file_path, query_footnotes_id) or []
                
                footnotes_results = []
                for footnote_id in footnote_ids: 
                    footnote_id = footnote_id.replace("#", "")    
                    query_footnotes = f'//li[@id="{footnote_id}"]/*/text()'
                    footnotes_results.append(execute_xpath_query(file_path, query_footnotes) or [])

#                if footnotes_results != []:
#                    footnotes_results = html_array_to_text(footnotes_results)
#                print("footnotes ", footnotes_results)
                

                caption_results = execute_xpath_query(file_path, query_caption) or []
                table_results = execute_xpath_query(file_path, query_table) or []
                reference_results_raw = execute_xpath_query(file_path, query_references) or []

                reference_results = []
                for elem in reference_results_raw:
                    reference_results.append(html_to_text(etree.tostring(elem, pretty_print=True).decode("utf-8")))

                if table_results:
                    table_html = ''.join([etree.tostring(result, pretty_print=True).decode() for result in table_results])
                else:
                    table_html = None

                file_results[table_id] = {
                    "caption": ' '.join(caption_results) if caption_results else None,
                    "table": table_html,
                    "footnotes": footnotes_results,
                    "references": reference_results
                }

            # Creare il nome del file JSON in base al file HTML
            json_file_name = os.path.splitext(file_name)[0] + '.json'
            json_file_path = os.path.join(extraction_path, json_file_name)

            # Salva i risultati in un file JSON specifico per il file HTML corrente
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(file_results, json_file, ensure_ascii=False, indent=4)

            print(f"Risultati salvati nel file '{json_file_name}' nella cartella 'extractions'.")

# Eseguire il ciclo su tutti i file HTML
process_all_html_files()
