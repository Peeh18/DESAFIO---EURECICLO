import zipfile
import os
import tempfile

def extract_zip(zip_path):
    extracted = []

    # Abre o arquivo .zip no caminho que foi recebido
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Cria uma pasta temporária para extrair os arquivos
        temp_dir = tempfile.mkdtemp()
        zip_ref.extractall(temp_dir) # Extrai tudo que esta dentro do zip para essa pasta

        # Percorre os arquivos extraídos
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if file.endswith('.xml'):
                    extracted.append(os.path.join(root, file))
                    
    return extracted