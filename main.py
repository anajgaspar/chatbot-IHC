from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="qwen3:0.6b")

template = """
Você é um assistente de biblioteca que fala apenas em português.
Responda de forma objetiva e direta.
Não invente livros ou autores. Só use informações reais do catálogo.
Estes são os livros disponíveis na biblioteca:
{catalogo_texto}
Responda apenas usando esta lista.
Não explique seu raciocínio. Apenas responda diretamente à pergunta. 
Se a pergunta não puder ser respondida com os livros disponíveis, responda "Desculpe, não tenho essa informação."

Pergunta do usuário: {pergunta}
"""

livros_disponiveis = [
    {"titulo": "Crime e Castigo", "autor": "Dostoiévski", "genero": "Romance psicológico"},
    {"titulo": "O Idiota", "autor": "Dostoiévski", "genero": "Romance"},
    {"titulo": "Os Irmãos Karamázov", "autor": "Dostoiévski", "genero": "Romance"}
]

catalogo_texto = "\n".join([f"{l['titulo']} - {l['autor']} ({l['genero']})" for l in livros_disponiveis])

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n=== Assistente de Biblioteca ===")
    pergunta = input("Pergunte alguma coisa (0 para sair): ")
    print("\n")
    if pergunta == "0":
        break
    resposta = chain.invoke({
        "catalogo_texto": catalogo_texto,
        "pergunta": pergunta
    })
    if "<think>" in resposta:
        resposta = resposta.split("</think>")[-1].strip()
    print(f"Usuário: {pergunta}\nAssistente: {resposta}")


