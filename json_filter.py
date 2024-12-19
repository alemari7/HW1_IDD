import json
import os

def filter_jsons_by_table_count(input_dir, output_dir, min_tables=3, max_tables=5):
    """
    Filtra i file JSON in una directory mantenendo solo quelli che contengono un numero di elementi
    compreso tra min_tables e max_tables.

    :param input_dir: Directory contenente i file JSON di input.
    :param output_dir: Directory dove salvare i file JSON filtrati.
    :param min_tables: Numero minimo di elementi richiesto.
    :param max_tables: Numero massimo di elementi consentito.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.json'):
            input_file = os.path.join(input_dir, file_name)
            output_file = os.path.join(output_dir, file_name)

            try:
                with open(input_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                element_count = len(data)

                if min_tables <= element_count <= max_tables:
                    with open(output_file, 'w', encoding='utf-8') as f_out:
                        json.dump(data, f_out, indent=4, ensure_ascii=False)

                    print(f"File {file_name} soddisfa i criteri e viene salvato in {output_dir}.")
                else:
                    print(f"File {file_name} non soddisfa i criteri.")
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Errore con il file {file_name}: {e}")

# Esempio di utilizzo
input_dir = 'json_cleaned'  # Directory dei file JSON di input
output_dir = 'json_filtered'  # Directory dei file JSON di output
filter_jsons_by_table_count(input_dir, output_dir)
