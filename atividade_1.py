import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = 'https://newsapi.org/v2/everything'


api_key = os.getenv("api_key")

if not api_key:
    raise ValueError("API Key não encontrada!")

#pronta
def menu():
    try:
        print("Seja bem-vindo ao consultor de notícias!")
        op_usuario = int(input("Digite: \n1-Consultar notícias \n2 - Sair"))
        if op_usuario == 1 or op_usuario == 2:
            return op_usuario
        else:
             print("Digite um número inteiro entre 1 e 2")
    except ValueError:
        print("Digite um número inteiro entre 1 - Consultar ou 2 - Sair!")

#pronta
def requerir_qtd_noticias():
    try:
        qtd_noticias = int(input("Digite quantas notícias deseja obter. (Mín 1 e Max 10)"))
        if qtd_noticias > 0 and qtd_noticias <= 10:
            return qtd_noticias
        else: 
            print("Digite um número inteiro para definir a quantidade de notícias (Mín 1 e Max 10)")
    except ValueError:
        print("Digite um número inteiro para definir a quantidade de notícias")

#ainda não pronta V
def requerir_tema_noticias():
    try:
        tema_noticia = int(input("Digite o tema que deseja: \n1 - Negócios, 2 - Entreterimento, 3 - Geral, 4 - Saúde \n"
                                "5 - Ciência, 6 - Esportes, 7 - Tecnologia"))
        if tema_noticia == 1:
            ...
        elif tema_noticia == 2:
            ...
        elif tema_noticia == 3:
            ...
        elif tema_noticia == 4:
            ...
        elif tema_noticia == 5:
            ...
        elif tema_noticia == 6:
            ...
        elif tema_noticia == 7:
            ...
        else:
            print("Digite um número inteiro de 1 - 7 para definir os temas das notícias")

    except ValueError:
        print("Digite um número inteiro de 1 - 7 para definir os temas das notícias")



