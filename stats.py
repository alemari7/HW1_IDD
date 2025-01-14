import os
import json

def calcola_statistiche_json(cartella):
    totale_elementi = 0
    tabelle_totali = 0
    tabelle_null = 0
    footnotes_vuote = 0
    references_vuote = 0
    totale_references = 0
    tabelle_con_table_non_null = 0
    numero_file = 0
    
    # Scorriamo tutti i file nella cartella
    for file_name in os.listdir(cartella):
        if file_name.endswith('.json'):  # Verifichiamo che sia un file JSON
            file_path = os.path.join(cartella, file_name)
            try:
                with open(file_path, 'r') as f:
                    dati = json.load(f)
                    
                    if isinstance(dati, dict):  # Assicuriamoci che il JSON sia un dizionario
                        totale_elementi += len(dati.keys())  # Conta il numero di chiavi
                        
                        # Iteriamo sugli id e raccogliamo le statistiche
                        for tabella, contenuti in dati.items():
                            if 'table' in contenuti:
                                tabelle_totali += 1  # Conta ogni tabella
                                
                                # Verifica se la tabella è null
                                if contenuti.get('table') is None:
                                    tabelle_null += 1  # Conta solo le tabelle null
                                else:
                                    # Se la tabella non è null, conteggia references
                                    tabelle_con_table_non_null += 1
                                    totale_references += len(contenuti.get('references', []))  # Conta il numero di references

                                # Verifica se le footnotes sono vuote
                                if contenuti.get('footnotes') == []:
                                    footnotes_vuote += 1  # Conta le footnotes vuote

                                # Verifica se le references sono vuote
                                if contenuti.get('references') == []:
                                    references_vuote += 1  # Conta le references vuote

                    numero_file += 1
            except Exception as e:
                print(f"Errore durante la lettura del file {file_name}: {e}")
    
    # Calcolo delle statistiche
    # Media elementi (numero di tabelle per file JSON)
    media_elementi = tabelle_con_table_non_null / numero_file if numero_file > 0 else 0

    # Percentuale di tabelle con 'table' null
    percentuale_tabelle_null = (tabelle_null / tabelle_totali * 100) if tabelle_totali > 0 else 0

    # Percentuale di tabelle con footnotes vuote
    percentuale_footnotes_vuote = (footnotes_vuote / tabelle_totali * 100) if tabelle_totali > 0 else 0

    # Percentuale di tabelle con references vuote
    percentuale_references_vuote = (references_vuote / tabelle_totali * 100) if tabelle_totali > 0 else 0

    # Media del numero di references per tabelle non nulle
    media_references = totale_references / tabelle_con_table_non_null if tabelle_con_table_non_null > 0 else 0

    # Restituisce tutte le statistiche
    return {
        "media_elementi": media_elementi,
        "percentuale_tabelle_null": percentuale_tabelle_null,
        "percentuale_footnotes_vuote": percentuale_footnotes_vuote,
        "percentuale_references_vuote": percentuale_references_vuote,
        "media_references": media_references
    }

# Esegui la funzione specificando il percorso della cartella
cartella_json = 'json_cleaned'
statistiche = calcola_statistiche_json(cartella_json)

# Stampa tutte le statistiche
print(f"La media del numero di tabelle nei file JSON è: {statistiche['media_elementi']:.2f}")
print(f"La percentuale di tabelle con valore null è: {statistiche['percentuale_tabelle_null']:.2f}%")
print(f"La percentuale di tabelle con footnotes vuote è: {statistiche['percentuale_footnotes_vuote']:.2f}%")
print(f"La percentuale di tabelle con references vuote è: {statistiche['percentuale_references_vuote']:.2f}%")
print(f"La media del numero di references per tabelle non nulle è: {statistiche['media_references']:.2f}")
