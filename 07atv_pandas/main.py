from fastapi import FastAPI, HTTPException
from typing import Dict, Any
import pandas

app = FastAPI()


df = pandas.read_csv("./20250702_Pedidos_csv_2025.csv", encoding="utf-16", sep=";") #carrega o CSV como um DataFrame (tabela)

@app.get("/pedidos/{id_pedido}", response_model=Dict[str, Any])
def get_pedido(id_pedido: int):
  
    pedido = df.query("IdPedido == @id_pedido")   #filtra o DataFrame, retornando apenas as linhas onde IdPedido == ao valor da URL, retornando um novo DataFrame)

    if pedido.empty:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
   
    resultado = pedido.iloc[0].to_dict()  #converte a primeira (e única) linha do DataFrame para dicionário
    
    print("Pedido encontrado:", resultado)

    return resultado
