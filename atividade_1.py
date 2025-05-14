import requests
from dotenv import load_dotenv
import os

load_dotenv()

temas = {
    1: "business",
    2: "entertainment",
    3: "general",
    4: "health",
    5: "science",
    6: "sports",
    7: "technology"
}

url = 'https://newsapi.org/v2/top-headlines'

api_key = os.getenv('api_key')

if not api_key:
    raise ValueError("API Key não encontrada!")

def menu():
    try:
        print("\n\nSeja bem-vindo ao consultor de notícias!")
        op_usuario = int(input("Digite: \n1 - Consultar notícias \n2 - Sair\n> "))
        if op_usuario in [1, 2]:
            return op_usuario
        else:
            print("Digite um número inteiro entre 1 e 2")
    except ValueError:
        print("Digite um número inteiro válido (1 ou 2).")

def requerir_qtd_noticias():
    global qtd_noticias
    try:
        qtd_noticias = int(input("Digite quantas notícias deseja obter. (Mín 1 e Max 10)\n> "))
        if 1 <= qtd_noticias <= 10:
            return qtd_noticias
        else: 
            print("Digite entre 1 e 10.")
    except ValueError:
        print("Digite um número inteiro válido.")

def requerir_tema_noticias():
    global tema_noticia
    try:
        tema_noticia = int(input("Escolha o tema que deseja:\n"
                                    "1 - Negócios\n2 - Entretenimento\n3 - Geral\n4 - Saúde\n"
                                    "5 - Ciência\n6 - Esportes\n7 - Tecnologia\n> "))
        if tema_noticia in temas:
            return temas[tema_noticia]
        else:
            print("Digite um número entre 1 e 7.")
    except ValueError:
        print("Digite um número inteiro válido.")

def puxar_noticias(tema_noticia, qtd_noticias):

    params = {
        'apiKey': api_key,
        'category': tema_noticia,
        'pageSize': qtd_noticias
    }

    resposta = requests.get(url=url, params=params)

    print(f"Status Code: {resposta.status_code}")
    if resposta.status_code == 200:
        dados = resposta.json() 
        artigos = dados.get('articles', [])
        if artigos:
            for i, artigo in enumerate(artigos, start=1):
                print(f"\nNotícia {i}:")
                print(f"Título: {artigo.get('title')}")
                print(f"Fonte: {artigo.get('source', {}).get('name')}")
                print(f"Link: {artigo.get('url')}")
        else:
            print("Nenhuma notícia encontrada.")
    else:
        print(f"Erro ao buscar notícias: {resposta.status_code} - {resposta.text}")

# Execução principal
while True:
    opcao = menu()
    if opcao == 1:
        tema = requerir_tema_noticias()
        qtd = requerir_qtd_noticias()
        puxar_noticias(tema, qtd) 
    else:
        print("Programa encerrado.")
        break
