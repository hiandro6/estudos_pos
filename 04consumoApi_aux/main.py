import requests, json

if __name__ == "__main__":
    url = "http://127.0.0.1:8000"
    while True:
        option = input("""
        ===========MENU=============
        1 - Listar todos os livros
        2 - Pesquisar livro por título
        3 - Cadastrar um livro
        4 - Deletar um livro
        5 - Editar um livro
        6 - Sair

        qual operação deseja realizar?""")


        if option == "1":
            r = requests.get(f"{url}/livros")
            livros = json.loads(r.text)
            
            for livro in livros:
                print(f"Título: {livro['titulo']}")
                print(f"Ano: {livro['ano']}")
                print(f"Edição: {livro['edicao']}")
                print("-" * 30)


        elif option == "2":
            pesquisa = input("Título do livro a ser buscado: ")
            r = requests.get(f"{url}/livros/{pesquisa}")

            print("Status Code:", r.status_code)

            if r.status_code == 200:
                livro = r.json()
                print(f"Título: {livro['titulo']}")
                print(f"Ano: {livro['ano']}")
                print(f"Edição: {livro['edicao']}")
                print("-" * 30)
            else:
                print("Livro não encontrado!")
        

        elif option == "3":
            titulo = input("digite o título do livro: ")
            ano = int(input("digite o ano do livro: "))
            edicao = int(input("digite a edição do livro: "))
            livro = {
                "titulo": titulo,
                "ano": ano,
                "edicao": edicao
            }
            r = requests.post(f"{url}/livros", json=livro)
            print(r.status_code)
            print(r.text)
        

        elif option == "4":
            pesquisa = input("título do livro a ser deletado: ")
            r = requests.delete(f"{url}/livros/{pesquisa}")
            print(r.status_code)


        elif option == "5":
            titulo_velho = input("digite o título do livro que deseja editar: ")
            titulo = input("digite o novo título do livro: ")
            ano = int(input("digite o novo ano do livro: "))
            edicao = int(input("digite a nova edição do livro: "))
            livro = {
                "titulo": titulo,
                "ano": ano,
                "edicao": edicao
            }
            r = requests.put(f"{url}/livros/{titulo_velho}", json=livro)
            print(r.status_code)
            print(r.text)
        

        elif option == "6":
            print("muito obrigado por usar nosso sistema, volte sempre!")
            break
        

        else:
            print("opção inválida tente novamente")