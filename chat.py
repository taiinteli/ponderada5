import os
import gradio as gr
import random
from dotenv import load_dotenv
# from langchain.llms import OpenAI
from langchain.llms import Ollama

# API Key ChatGPT
load_dotenv()
# api_key = os.getenv('OPENAI_API_KEY')

# Função para recuperar o documento
def retrieve_document():
    with open("ponderada5_txt.txt", "r") as f:
        return f.read()

# Configuração do modelo LLM com streaming
# llm = OpenAI(api_key=api_key, model="gpt-3.5-turbo-instruct", max_tokens=512)
llm = Ollama(model="mistral") 

def preparar_prompt(pergunta):
    documento = retrieve_document()
    return f"""
    Pergunta do usuário: '{pergunta}'
    Contexto:
        {documento}
    """

def chatbot(pergunta):
    resposta = ""
    for chunk in llm.stream(preparar_prompt(pergunta)):
        resposta += chunk
    return resposta

def random_response(message, history):
    return random.choice(["Olá, como posso ajudar?", " oi "])


def is_question(message):
    if message[-1] == "?":
        return True
    return False


#Gradio interface
def interface(message, history):
    if is_question(message):
        resposta = chatbot(message)
    else:
        resposta = random_response(message, history)
    return resposta

demo = gr.ChatInterface(interface)

demo.launch()