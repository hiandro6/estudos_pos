from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Session, create_engine, select
from contextlib import asynccontextmanager
from typing import Annotated, Dict, Any
import pandas as pd
from models import Pedido
from datetime import datetime

sqlite_file_name = "pedidos.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def importar_csv():
    df = pd.read_csv("./20250702_Pedidos_csv_2025.csv", encoding="utf-16", sep=";")

    def converter_data(valor):
        try:
            return datetime.strptime(valor, "%d/%m/%Y").date()
        except:
            return None  # se a data estiver em branco

    df["DataRegistro"] = df["DataRegistro"].apply(converter_data)
    df["PrazoAtendimento"] = df["PrazoAtendimento"].apply(converter_data)
    df["DataResposta"] = df["DataResposta"].apply(converter_data)

    with Session(engine) as session:
        for _, row in df.iterrows():
            dados = row.to_dict()
            pedido = Pedido(**dados)
            session.merge(pedido)
        session.commit()


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    importar_csv()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/pedidos/{id_pedido}", response_model=Dict[str, Any])
def get_pedido(id_pedido: int, session: SessionDep):
    pedido = session.exec(select(Pedido).where(Pedido.IdPedido == id_pedido)).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido.dict()
