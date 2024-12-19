import json
import os

def filter_json_by_key(input_file, output_file):
    """
    Filtra un file JSON mantenendo solo gli elementi le cui chiavi contengono la lettera 'T'.

    :param input_file: Path al file JSON di input.
    :param output_file: Path al file JSON di output con i dati filtrati.
    """
    try:
        # Leggi il file JSON di input
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Filtra gli elementi che hanno una 'T' nella chiave
        filtered_data = {key: value for key, value in data.items() if 'T' in key}

        # Scrivi il risultato nel file di output
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, indent=4, ensure_ascii=False)

        print(f"Dati filtrati salvati in {output_file}")
    except FileNotFoundError:
        print(f"Errore: Il file {input_file} non esiste.")
    except json.JSONDecodeError:
        print(f"Errore: Il file {input_file} non è un file JSON valido.")

def filter_jsons_in_directory(input_dir, output_dir):
    """
    Filtra tutti i file JSON in una directory, salvando i risultati in un'altra directory.

    :param input_dir: Directory contenente i file JSON di input.
    :param output_dir: Directory dove salvare i file JSON filtrati.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.json'):
            input_file = os.path.join(input_dir, file_name)
            output_file = os.path.join(output_dir, file_name)
            filter_json_by_key(input_file, output_file)

# Esempio di utilizzo
input_dir = 'extractions'  # Directory dei file JSON di input
output_dir = 'json_cleaned'  # Directory dei file JSON di output
filter_jsons_in_directory(input_dir, output_dir)
