import os
import json
from lxml import etree

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
    all_results = {}  # Dizionario per memorizzare i risultati di tutti i file HTML
    
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
                query_caption = f'//table[@id="{table_id}"]/ancestor::figure//figcaption/text()'
                query_table = f'//table[@id="{table_id}"]/ancestor::figure//table'
                query_footnotes = f'//table[@id="{table_id}"]/ancestor::figure//sup/text()'
                query_references = f"//*[substring(@href, string-length(@href) - string-length('#{table_id}') + 1) = '#{table_id}']/ancestor::p/text()"
                
                # Eseguire le query e raccogliere i risultati
                caption_results = execute_xpath_query(file_path, query_caption) or []
                table_results = execute_xpath_query(file_path, query_table) or []
                footnote_results = execute_xpath_query(file_path, query_footnotes) or []
                reference_results = execute_xpath_query(file_path, query_references) or []

                # Convertire i risultati della tabella in formato HTML
                if table_results:
                    table_html = ''.join([etree.tostring(result, pretty_print=True).decode() for result in table_results])
                else:
                    table_html = None

                # Creare un dizionario per i risultati di questo ID
                file_results[table_id] = {
                    "caption": ' '.join(caption_results) if caption_results else None,
                    "table": table_html,
                    "footnotes": footnote_results,
                    "references": reference_results
                }

            # Aggiungere i risultati di questo file al dizionario generale
            all_results[file_name] = file_results

    # Salva i risultati in un file JSON
    with open('table_results.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_results, json_file, ensure_ascii=False, indent=4)
    
    print("\nRisultati salvati nel file 'table_results.json'.")

# Eseguire il ciclo su tutti i file HTML
process_all_html_files()
