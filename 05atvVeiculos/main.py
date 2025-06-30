from fastapi import FastAPI, HTTPException
from models import Veiculo
from typing import List

app = FastAPI()
veiculos:List[Veiculo] = []

@app.get("/veiculos",response_model=List[Veiculo])
def listar_veiculos():
    return veiculos

@app.get("/veiculos/{placa}",response_model=Veiculo)
def listar_veiculo(placa:str):
    for veiculo in veiculos:
        if veiculo.placa == placa:
            return veiculo
    raise HTTPException(404,"Não localizado")

@app.post("/veiculos", response_model=Veiculo)
def criar_veiculo(veiculo:Veiculo):
    veiculos.append(veiculo)
    return veiculo

@app.delete("/veiculos/{placa}",response_model=Veiculo)
def deletar_veiculo(placa:str):
    for pos, veiculo in enumerate(veiculos):
        if veiculo.placa == placa:
            veiculos.pop(pos)
            return veiculo
    raise HTTPException(404,"Não localizado")

@app.put("/veiculos/{placa}", response_model=Veiculo)
def editar_veiculo(placa:str, novoVeiculo: Veiculo):
    for veiculo in veiculos:
        if veiculo.placa == placa:
            veiculo.placa = novoVeiculo.placa
            veiculo.nome = novoVeiculo.nome
            veiculo.marca = novoVeiculo.marca
            veiculo.modelo = novoVeiculo.modelo
            return veiculo
    raise HTTPException(404, "Não localizado")