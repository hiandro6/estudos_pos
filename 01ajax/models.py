from pydantic import BaseModel
from typing import List
from datetime import date

class Usuario(BaseModel):
    id: int
    username:str
    password:str
    data_criacao:date

class Livro(BaseModel):
    id: int
    titulo:str
    ano:int
    edicao:int

class LivroCreate(BaseModel):
    titulo:str
    ano:int
    edicao:int


class Emprestimo(BaseModel):
    id: int
    usuario:Usuario
    livro:Livro
    data_emprestimo:date
    data_devolucao:date

class Biblioteca(BaseModel):
    id: int
    nome:str
    acervo: List["Livro"]
    usuarios: List["Usuario"]
    emprestimos: List["Emprestimo"]