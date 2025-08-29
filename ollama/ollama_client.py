import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3"

def gerar_resposta_ollama(prompt):
    response = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt})
    return response.json()['response']
