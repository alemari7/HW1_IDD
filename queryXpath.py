from lxml import etree

# Funzione per eseguire una query XPath su un file XML o HTML
def execute_xpath_query(file_path, xpath_query):
    # Leggere il file
    try:
        with open(file_path, 'rb') as f:
            # Parsing del file con lxml
            tree = etree.parse(f)
            
            # Esecuzione della query XPath
            results = tree.xpath(xpath_query)
            
            # Mostrare i risultati della query
            print("Risultati della query XPath:")
            for result in results:
                if isinstance(result, etree._Element):
                    # Se è un elemento HTML/XML, stampare l'intero testo
                    print(etree.tostring(result, pretty_print=True).decode())
                else:
                    # Se è un semplice valore, stamparlo
                    print(result)
                    return result
    except Exception as e:
        print(f"Errore nell'eseguire la query XPath: {e}")

# Esempio di utilizzo
file_path = 'sources/' + 'html-2410.04936.html' 
query_id        = '//table[@id="S2.T1.1"]/ancestor::figure/@id'
query_caption   = '//table[@id="S2.T1.1"]/ancestor::figure//figcaption/text()'
query_table     = '//table[@id="S2.T1.1"]/ancestor::figure//table'   
query_footnotes = '//table[@id="S2.T1.1"]/ancestor::figure//sup/text()'   
           


# Eseguire la query
execute_xpath_query(file_path, query_caption)
print("--------------------------------------------------------------------------------------")
execute_xpath_query(file_path, query_table)
print("--------------------------------------------------------------------------------------")
id= execute_xpath_query(file_path, query_id)
query_references= f"//*[substring(@href, string-length(@href) - string-length('#{id}') + 1) = '#{id}']/ancestor::p/text()"    
print("--------------------------------------------------------------------------------------")
execute_xpath_query(file_path, query_references)
print("--------------------------------------------------------------------------------------")
execute_xpath_query(file_path, query_footnotes)
