
from sqlmodel import SQLModel, Field

class Aluno(SQLModel, table = True):
    matricula : str = Field(primary_key=True)
    nome: str = Field(index=False)
    curso: str = Field(index=False)