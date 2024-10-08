import requests
from bs4 import BeautifulSoup
import os
import re

# Creare una cartella per i file scaricati
os.makedirs("sources", exist_ok=True)

# URL della pagina del topic
url = 'https://arxiv.org/list/cs.AI/recent?skip=0&show=2000'

# Limite di file da scaricare
file_limit = 5

# Richiesta HTTP alla pagina principale
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Trova tutti i link che portano ai file HTML
html_links = soup.find_all('a', href=True)

# Estrarre solo i link con id che iniziano con "html-" e creare un'etichetta
html_filtered_links = []
for link in html_links:
    href = link.get('href')     # Estrai l'URL
    id_attr = link.get('id')    # Estrai l'ID
    
    # Controlla che l'id inizi con 'html-' e il link sia valido
    if id_attr and id_attr.startswith('html-') and href.startswith('https'): 
        # Estrarre nome del file dopo 'html-'
        file_name = re.search(r'html-(\d+\.\d+)', id_attr)  # Cerca il pattern 'html-<numero>.<numero>'
        if file_name:                                       # Se il pattern è stato trovato, aggiungi il nome del file e l'URL alla lista
            html_filtered_links.append((file_name.group(1), href)) 

# Limita il numero di file da scaricare se necessario
html_filtered_links = html_filtered_links[:file_limit]

# Scarica i file HTML e salvali con l'etichetta corretta
for file_name, link in html_filtered_links:
    html_response = requests.get(link)                                  # Richiesta HTTP al file HTML
    file_path = os.path.join("sources", f"html-{file_name}.html")       # Percorso del file
    
    # Scrivi il contenuto HTML in un file
    with open(file_path, 'w', encoding='utf-8') as file:                # Apri il file in modalità scrittura
        file.write(html_response.text)                                  # Scrivi il contenuto HTML nel file
        print(f"File salvato: {file_path}")                                 
