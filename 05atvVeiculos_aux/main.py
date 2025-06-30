import requests
import json

if __name__ == "__main__":
    url = "http://127.0.0.1:8000"
    while True:
        option = input("""
        ===========MENU=============
        1 - Listar todos os veículos
        2 - Pesquisar veículo por placa
        3 - Cadastrar um veículo
        4 - Deletar um veículo
        5 - Editar um veículo
        6 - Sair

        Qual operação deseja realizar? """)

        if option == "1":
            r = requests.get(f"{url}/veiculos")
            if r.status_code == 200:
                veiculos = r.json()
                for veiculo in veiculos:
                    print(f"Nome: {veiculo['nome']}")
                    print(f"Marca: {veiculo['marca']}")
                    print(f"Modelo: {veiculo['modelo']}")
                    print(f"Placa: {veiculo['placa']}")
                    print("-" * 30)
            else:
                print("Erro ao buscar veículos.")

        elif option == "2":
            placa = input("Placa do veículo a ser buscado: ")
            r = requests.get(f"{url}/veiculos/{placa}")

            print("Status Code:", r.status_code)

            if r.status_code == 200:
                veiculo = r.json()
                print(f"Nome: {veiculo['nome']}")
                print(f"Marca: {veiculo['marca']}")
                print(f"Modelo: {veiculo['modelo']}")
                print(f"Placa: {veiculo['placa']}")
            else:
                print("Veículo não encontrado!")

        elif option == "3":
            nome = input("Digite o nome do veículo: ")
            marca = input("Digite a marca do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            placa = input("Digite a placa do veículo: ")
            veiculo = {
                "nome": nome,
                "marca": marca,
                "modelo": modelo,
                "placa": placa
            }
            r = requests.post(f"{url}/veiculos", json=veiculo)
            print(r.status_code)
            print(r.text)

        elif option == "4":
            placa = input("Placa do veículo a ser deletado: ")
            r = requests.delete(f"{url}/veiculos/{placa}")
            print(r.status_code)
            print(r.text)

        elif option == "5":
            placa_antiga = input("Digite a placa do veículo que deseja editar: ")
            nome = input("Digite o novo nome do veículo: ")
            marca = input("Digite a nova marca do veículo: ")
            modelo = input("Digite o novo modelo do veículo: ")
            nova_placa = input("Digite a nova placa do veículo: ")
            veiculo = {
                "nome": nome,
                "marca": marca,
                "modelo": modelo,
                "placa": nova_placa
            }
            r = requests.put(f"{url}/veiculos/{placa_antiga}", json=veiculo)
            print(r.status_code)
            print(r.text)

        elif option == "6":
            print("Muito obrigado por usar nosso sistema, volte sempre!")
            break

        else:
            print("Opção inválida. Tente novamente.")
