import os
from bs4 import BeautifulSoup

# Percorso della cartella
cartella = 'sources'

# Scansione dei file nella cartella
for nome_file in os.listdir(cartella):
    if nome_file.endswith('.html'):
        percorso_file = os.path.join(cartella, nome_file)
        
        # Apertura del file e analisi del contenuto
        with open(percorso_file, 'r', encoding='utf-8') as file:
            contenuto = file.read()
            soup = BeautifulSoup(contenuto, 'html.parser')
            
            # Controllo se il tag <title> contiene "403 Forbidden"
            titolo = soup.title.string if soup.title else ''
            if titolo == '403 Forbidden':
                # Eliminazione del file
                os.remove(percorso_file)
                print(f'File eliminato: {percorso_file}')
             # Controllo se il contenuto contiene "rate exceeded"
            if 'rate exceeded' in soup.get_text().lower():
                # Eliminazione del file
                os.remove(percorso_file)
                print(f'File eliminato x: {percorso_file}')
