import requests
from bs4 import BeautifulSoup
import os
import re

# Creare una cartella per i file scaricati
os.makedirs("sources", exist_ok=True)

# URL della pagina del topic
file_limit = 200

url = 'https://arxiv.org/search/advanced?advanced=1&terms-0-term=machine+translation&terms-0-operator=AND&terms-0-field=title&classification-computer_science=y&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size=200&order=&start=600'

# Richiesta HTTP alla pagina principale
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Trova tutti i link che contengono '/abs/' nell'href
abs_links = soup.find_all('a', href=re.compile(r'/abs/'))
#print(len(abs_links))

# Filtra e modifica i link sostituendo '/abs/' con '/html/'
html_filtered_links = []
for link in abs_links:
    href = link.get('href')
    
    # Modifica il link sostituendo '/abs/' con '/html/'
    html_link = href.replace('/abs/', '/html/')
    
    
    # Crea un'etichetta per il file basata sull'ultimo segmento del link
    file_name = html_link.split('/')[-1]  # L'ID del documento
    html_link  # Costruisce il link completo
    
    # Aggiungi il nome del file e l'URL alla lista
    html_filtered_links.append((file_name, html_link))

# Limita il numero di file da scaricare se necessario
html_filtered_links = html_filtered_links[:file_limit]

# Scarica i file HTML e salvali con l'etichetta corretta
for file_name, link in html_filtered_links:
    html_response = requests.get(link)                                  # Richiesta HTTP al file HTML
    file_path = os.path.join("sources", f"{file_name}.html")            # Percorso del file
    
    # Scrivi il contenuto HTML in un file
    with open(file_path, 'w', encoding='utf-8') as file:                # Apri il file in modalità scrittura
        file.write(html_response.text)                                  # Scrivi il contenuto HTML nel file
        print(f"File salvato: {file_path}")
