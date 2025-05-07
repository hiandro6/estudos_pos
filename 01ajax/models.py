from pydantic import BaseModel
from typing import List
from datetime import datetime

class Usuario(BaseModel):
    id: int
    username:str
    password:str
    data_criacao:datetime

class Livro(BaseModel):
    id: int
    titulo:str
    ano:int
    edicao:int

class Biblioteca(BaseModel):
    id: int
    nome:str
    acervo: List["Livro"]
    usuario: List["Usuario"]

class Emprestimo(BaseModel):
    id: int
    usuario:Usuario
    livro:Livro
    data_emprestimo:datetime
    data_devolucao:datetime