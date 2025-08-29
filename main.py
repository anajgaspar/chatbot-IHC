import asyncio
from mindsdb_sdk import SDK
from ollama.ollama_client import gerar_resposta_ollama

mdb = SDK("http://localhost:47334")
project = mdb.get_project("mindsdb")

