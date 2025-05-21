from fastapi import FastAPI,HTTPException
from models import Carro, Cliente, Reserva, CarroEsqueleto, ClienteEsqueleto, ReservaEsqueleto
from typing import List
import datetime

app = FastAPI()


carros: List[Carro] = []
count_id_car = 1
clientes: List[Cliente] = []
count_id_cli = 1
reservas: List[Reserva] = []
count_id_res = 1

#carros
@app.get("/carros",response_model=List[Carro])
def listar_carros():
    return carros

@app.post("/carros", response_model=Carro)
def criar_carro(carro: CarroEsqueleto):
    global count_id_car
    novo_carro = Carro(id=count_id_car, **carro.model_dump())
    carros.append(novo_carro)
    count_id_car += 1
    return novo_carro


@app.put("/carros/{id}",response_model=Carro)
def atualizar_carro(id: int, dados: CarroEsqueleto):
    for c in carros:
        if c.id == id:
            c.modelo = dados.modelo
            c.marca = dados.marca
            c.ano = dados.ano
            c.disponivel = dados.disponivel
            return c
    raise HTTPException(404,"Não localizado.")

@app.delete("/carros/{id}",response_model=Carro)
def deletar_carro(id: int):
    for i, c in enumerate(carros):
        if c.id == id:
            carro_removido = carros.pop(i)
            return carro_removido
    raise HTTPException(404,"Não localizado.")



#clientes:
@app.get("/clientes",response_model=List[Cliente])
def listar_clientes():
    return clientes

@app.post("/clientes", response_model=Cliente)
def criar_cliente(cliente: ClienteEsqueleto):
    global count_id_cli
    novo_cliente = Cliente(id=count_id_cli, **cliente.model_dump())
    clientes.append(novo_cliente)
    count_id_cli += 1
    return novo_cliente


@app.get("/clientes/{id}",response_model=Cliente)
def listar_cliente(id: int):
    for c in clientes:
        if c.id == id:
            return c
    raise HTTPException(404,"Não localizado.")



#reservas:
@app.post("/reservas", response_model=Reserva)
def criar_reserva(reserva: ReservaEsqueleto):
    global count_id_res

    cliente = None #verificar se o cliente existe
    for cli in clientes:
        if cli.id == reserva.cliente_id:
            cliente = cli
            break
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    

    carro = None #verificar se o cliente existe e está disponível
    for car in carros:
        if car.id == reserva.carro_id:
            carro = car
            break
    if not carro:
        raise HTTPException(status_code=404, detail="Carro não encontrado.")
    elif not carro.disponivel:
        raise HTTPException(status_code=400, detail="Carro indisponível.")
    
    if reserva.data_fim < reserva.data_inicio:
        raise HTTPException(status_code=400, detail="Data de fim não pode ser antes da data de início.")
    
    carro.disponivel = False

    nova_reserva = Reserva(id=count_id_res, **reserva.model_dump())
    reservas.append(nova_reserva)
    count_id_res += 1
    return nova_reserva


@app.get("/reservas",response_model=List[Reserva])
def listar_reservas():
    return reservas

@app.delete("/reservas/{id}",response_model=Reserva)
def deletar_reserva(id: int):
    for i, res in enumerate(reservas):
        if res.id == id:
            for car in carros:
                if car.id == res.carro_id:
                    car.disponivel = True
                    break

            reserva_deletada = reservas.pop(i)
            return reserva_deletada
    raise HTTPException(404,"reserva não localizada")
