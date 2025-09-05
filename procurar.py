import os
from db import modelo

def obter_arquivo_para_download(titulo):
    # Busca o livro no MindsDB
    resultado = modelo.query(f"SELECT * FROM biblioteca_model WHERE titulo LIKE '%{titulo}%'")
    
    if resultado:
        arquivo = resultado[0]['arquivo']
        caminho = os.path.join('livros', arquivo)
        if os.path.exists(caminho):
            return caminho  # caminho do arquivo para enviar
        else:
            return "Arquivo não encontrado no servidor."
    else:
        return "Livro não encontrado na biblioteca."

# Teste
titulo_usuario = "Crime e Castigo"
arquivo = obter_arquivo_para_download(titulo_usuario)
print("Arquivo para download:", arquivo)