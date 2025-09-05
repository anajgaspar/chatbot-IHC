import mindsdb_sdk
import pandas as pd

client = mindsdb_sdk.Client()
db_model = client.get_model('biblioteca_model')

dados_livros = [
    {"titulo": "Crime e Castigo", "autor": "Dostoiévski", "genero": "Romance psicológico", "arquivo": "Crime_e_Castigo.pdf"},
    {"titulo": "O Idiota", "autor": "Dostoiévski", "genero": "Romance", "arquivo": "O_Idiota.pdf"},
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "genero": "Romance", "arquivo": "Dom_Casmurro.pdf"}
]

df_livros = pd.DataFrame(dados_livros)

client.create_datasource(
    name="biblioteca_model",  # nome da tabela/modelo
    data=df_livros,
    overwrite=True  # se já existir, substitui
)

print("Tabela criada e dados inseridos com sucesso!")

# 3️⃣ Função para buscar livros no MindsDB
def buscar_livros(autor=None):
    query = "SELECT titulo, autor, genero FROM biblioteca_model"
    if autor:
        query += f" WHERE autor LIKE '%{autor}%'"
    resultados = db_model.query(query)
    return resultados

# 5️⃣ Testar consulta
modelo = client.get_model('biblioteca_model')
resultado = modelo.query("SELECT * FROM biblioteca_model WHERE autor='Dostoiévski'")
print("Consulta de teste:")
print(resultado)