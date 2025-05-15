import requests

# Simulando um banco de dados de usuários
usuarios = {
    1: {'email': 'lara@gmail.com', 'senha': '123'},
    2: {'email': 'carol@gmail.com', 'senha': '456'},
    3: {'email': 'joyce@gmail.com', 'senha': '789'}
}

# Contadores de interações
interacoes = {
    'posts_visualizados': 0,
    'comentarios_visualizados': 0,
    'posts_criados': 0
}

# Função para login
def login():
    print("Login:")
    email = input("Email: ")
    senha = input("Senha: ")

    for codigo, info in usuarios.items():
        if info['email'] == email and info['senha'] == senha:
            print(f"Login bem-sucedido! Bem-vindo(a), {email}")
            return codigo
    print("Login inválido.")
    return None

# Funções de ações
def visualizar_posts():
    resposta = requests.get("https://jsonplaceholder.typicode.com/posts")
    if resposta.status_code == 200:
        posts = resposta.json()
        for post in posts[:5]:  # Mostra os 5 primeiros
            print(f"\nPost ID: {post['id']}")
            print(f"Título: {post['title']}")
            print(f"Corpo: {post['body']}")
        interacoes['posts_visualizados'] += 5
    else:
        print("Erro ao buscar posts.")

def visualizar_comentarios():
    post_id = input("Digite o ID do post para ver os comentários: ")
    resposta = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
    if resposta.status_code == 200:
        comentarios = resposta.json()
        for c in comentarios:
            print(f"\nComentário por {c['email']}")
            print(f"{c['body']}")
        interacoes['comentarios_visualizados'] += len(comentarios)
    else:
        print("Erro ao buscar comentários.")

def visualizar_meus_posts(user_id):
    resposta = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
    if resposta.status_code == 200:
        posts = resposta.json()
        print(f"Você tem {len(posts)} post(s).")
        for post in posts:
            print(f"\nPost ID: {post['id']}")
            print(f"Título: {post['title']}")
            print(f"Corpo: {post['body']}")
        interacoes['posts_visualizados'] += len(posts)
    else:
        print("Erro ao buscar seus posts.")

def filtrar_posts_por_usuario():
    user_id = input("Digite o ID do usuário (1 a 10): ")
    resposta = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
    if resposta.status_code == 200:
        posts = resposta.json()
        print(f"{len(posts)} post(s) encontrados.")
        for post in posts[:5]:  # Mostra os 5 primeiros
            print(f"\nPost ID: {post['id']}")
            print(f"Título: {post['title']}")
            print(f"Corpo: {post['body']}")
        interacoes['posts_visualizados'] += min(len(posts), 5)
    else:
        print("Erro ao buscar posts.")

def criar_post(user_id):
    print("=== Criar novo post ===")
    titulo = input("Título: ")
    corpo = input("Corpo do post: ")
    novo_post = {
        "userId": user_id,
        "title": titulo,
        "body": corpo
    }
    resposta = requests.post("https://jsonplaceholder.typicode.com/posts", json=novo_post)
    if resposta.status_code == 201:
        post = resposta.json()
        print(f"Post criado com ID: {post['id']}")
        interacoes['posts_criados'] += 1
    else:
        print("Erro ao criar post.")

# Função principal
def main():
    user_id = login()
    if not user_id:
        return
    else:
        while True:
            print("\n=== MENU ===")
            print("1 - Visualizar posts")
            print("2 - Visualizar comentários de um post")
            print("3 - Visualizar meus posts")
            print("4 - Filtrar posts por outro usuário")
            print("5 - Criar um novo post")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                visualizar_posts()
            elif opcao == '2':
                visualizar_comentarios()
            elif opcao == '3':
                visualizar_meus_posts(user_id)
            elif opcao == '4':
                filtrar_posts_por_usuario()
            elif opcao == '5':
                criar_post(user_id)
            elif opcao == '0':
                print("\n=== RESUMO DAS INTERAÇÕES ===")
                print(f"Posts visualizados: {interacoes['posts_visualizados']}")
                print(f"Comentários visualizados: {interacoes['comentarios_visualizados']}")
                print(f"Posts criados: {interacoes['posts_criados']}")
                print("Até logo!")
                break
            else:
                print("Opção inválida.")

# Executa o programa
if __name__ == "__main__":
    main()
