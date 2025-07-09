from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from models import Aluno
from sqlmodel import create_engine, SQLModel, Session, select
from typing import Annotated, List


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

#gerenciamento de sessão
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/alunos")
def aluno(session:SessionDep) -> List[Aluno]:
    alunos = session.exec(select(Aluno)).all()
    return alunos



@app.post("/aluno/")
def create_aluno( aluno: Aluno, session: SessionDep) -> Aluno:
    session.add(aluno)
    session.commit()
    session.refresh(aluno)
    return aluno