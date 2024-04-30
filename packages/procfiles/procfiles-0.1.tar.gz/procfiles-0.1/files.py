import os

def read_files_in_folders(caminho_pasta):
    """
    Lê todos os arquivos em uma pasta específica e retorna uma lista com seus nomes.
    
    Args:
        caminho_pasta (str): O caminho para a pasta contendo os arquivos.
    
    Returns:
        list: Uma lista com os nomes dos arquivos na pasta.
    """
    try:
        # Lista todos os arquivos na pasta
        arquivos = os.listdir(caminho_pasta)
        return arquivos
    except OSError as e:
        print(f"Erro ao ler os arquivos na pasta: {e}")
        return []
