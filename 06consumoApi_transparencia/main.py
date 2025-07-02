import os
import requests
from dotenv import load_dotenv

# Carrega o .env com o token
load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
if not ACCESS_TOKEN:
    raise ValueError("ACCESS_TOKEN não definido no arquivo .env")

BASE_URL = "https://api.portaldatransparencia.gov.br/api-de-dados"
headers = {
    "Authorization": ACCESS_TOKEN
}

def bolsa_familia():
    cpf = input("Digite o CPF ou NIS do beneficiário: ")
    mesAno = input("Digite o mês e ano no formato MMAAAA (ex: 052024): ")
    url = f"{BASE_URL}/bolsa-familia-por-cpf-ou-nis"
    params = {"codigoBeneficiario": cpf, "mesAno": mesAno}
    r = requests.get(url, headers=headers, params=params)
    print(r.status_code)
    print(r.json())

def bolsa_familia_por_id():
    id_registro = input("Digite o ID do registro do Bolsa Família: ")
    url = f"{BASE_URL}/bolsa-familia/{id_registro}"
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.json())

def garantia_safra():
    cpf = input("Digite o CPF ou NIS do beneficiário: ")
    mesAno = input("Digite o mês e ano no formato MMAAAA (ex: 052024): ")
    url = f"{BASE_URL}/garantia-safra-por-cpf-ou-nis"
    params = {"codigoBeneficiario": cpf, "mesAno": mesAno}
    r = requests.get(url, headers=headers, params=params)
    print(r.status_code)
    print(r.json())

def seguro_defeso():
    cpf = input("Digite o CPF ou NIS do beneficiário: ")
    mesAno = input("Digite o mês e ano no formato MMAAAA (ex: 052024): ")
    url = f"{BASE_URL}/seguro-defeso-por-cpf-ou-nis"
    params = {"codigoBeneficiario": cpf, "mesAno": mesAno}
    r = requests.get(url, headers=headers, params=params)
    print(r.status_code)
    print(r.json())

def servidor_federal():
    cpf = input("Digite o CPF do servidor público: ")
    url = f"{BASE_URL}/servidores/{cpf}"
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.json())

if __name__ == "__main__":
    while True:
        opcao = input("""
=========== MENU TRANSPARÊNCIA ===========
1 - Consultar Bolsa Família por CPF/NIS e Período
2 - Consultar registro do Bolsa Família por ID
3 - Consultar Garantia-Safra por CPF/NIS e Período
4 - Consultar Seguro Defeso por CPF/NIS e Período
5 - Consultar Servidor Público Federal por CPF
6 - Sair

Escolha uma opção: """)

        if opcao == "1":
            bolsa_familia()
        elif opcao == "2":
            bolsa_familia_por_id()
        elif opcao == "3":
            garantia_safra()
        elif opcao == "4":
            seguro_defeso()
        elif opcao == "5":
            servidor_federal()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")