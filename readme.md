# Documentação 

### Vídeo de funcionamento: https://drive.google.com/file/d/13XElCiFpcx62aX9NvE6ZWTRRYcmmVOdF/view?usp=sharing 

### O Chatbot LLM utiliza o modelo de linguagem natural Ollama e o Gradio para fornecer respostas a consultas dos usuários. Ele suporta dois modos de interação: consulta ao modelo Ollama para respostas sensíveis ao contexto e geração de respostas usando o modelo GPT-3.

### Envio de Solicitações para o Ollama
A função send_request2 é responsável por enviar perguntas para o modelo Ollama. Ela utiliza um contexto fornecido no arquivo "ponderada5_txt.txt" e um modelo Sentence Transformer pré-treinado ("all-MiniLM-L6-v2") para incorporações. A resposta é gerada passando a pergunta pelo modelo Ollama.

``` 
resposta = send_request2("qual é o significado da vida?")
print(resposta) 
```
 
### Passo 1: Instalação de Dependências
Certifique-se de ter as bibliotecas necessárias instaladas. Abra um terminal na pasta do projeto e execute o seguinte comando:

```
pip install gradio langchain sentence-transformers
```

### Passo 2: Arquivo de Contexto
Certifique-se de ter um arquivo chamado "ponderada5_txt.txt" na mesma pasta do script. Esse arquivo é utilizado como contexto para o modelo Ollama.

### Passo 3: Execução do Script
Execute o script Python. No terminal, navegue até a pasta do projeto e execute o seguinte comando:

```
python chat2.py
```


