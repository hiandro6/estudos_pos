from fastapi import FastAPI, HTTPException
from models import Usuario, Livro, LivroCreate, Biblioteca, Emprestimo
from typing import List

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Libera o acesso para todas as origens (origins="*")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, troque "*" por uma lista de URLs confiáveis
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# usuários:
usuarios: List[Usuario] = []
@app.get("/usuarios/", response_model=List[Usuario])
def listar_usuarios():
    return usuarios

@app.post("/usuarios/", response_model=Usuario)
def criar_usuario(usuario:Usuario):
    usuario.id = len(usuarios) + 1
    usuarios.append(usuario)
    return usuario

@app.delete("/usuarios/{usu_id}", response_model=Usuario)
def excluir_usuario(usu_id:int):
    for index, usuario in enumerate(usuarios):
        if usu_id == usuario.id:
            del usuarios[index]
            return usuario
    raise HTTPException(status_code=404, detail="Não localizado")


# livros:
livros: List[Livro] = []
@app.get("/livros/", response_model=List[Livro])
def listar_livros():
    return livros

@app.post("/livros/", response_model=Livro)
def criar_livro(livro:LivroCreate):
    novo_livro = Livro(
        id=len(livros) + 1,
        titulo=livro.titulo,
        ano=livro.ano,
        edicao=livro.edicao
    )

    livros.append(novo_livro)
    return novo_livro

@app.delete("/livros/{liv_id}", response_model=Livro)
def excluir_livro(liv_id:int):
    for index, livro in enumerate(livros):
        if liv_id == livro.id:
            del livros[index]
            return livro
    raise HTTPException(status_code=404, detail="Não localizado")



# biblioteca: 
bibliotecas: List[Biblioteca] = []
@app.get("/biblioteca/", response_model=List[Biblioteca])
def listar_bibliotecas():
    return bibliotecas

@app.post("/biblioteca/", response_model=Biblioteca)
def criar_biblioteca(biblioteca:Biblioteca):
    biblioteca.id = len(bibliotecas) + 1
    bibliotecas.append(biblioteca)
    return biblioteca

@app.delete("/biblioteca/{biblioteca_id}", response_model=Biblioteca)
def excluir_biblioteca(biblioteca_id:int):
    for index, biblioteca in enumerate(bibliotecas):
        if biblioteca_id == biblioteca.id:
            del bibliotecas[index]
            return biblioteca
    raise HTTPException(status_code=404, detail="Não localizado")





# empréstimmos: 
emprestimos: List[Emprestimo] = []
@app.get("/emprestimos/", response_model=List[Emprestimo])
def listar_emprestimos():
    return emprestimos

@app.post("/emprestimos/", response_model=Emprestimo)
def criar_emprestimo(emprestimo:Emprestimo):
    emprestimo.id = len(emprestimos) + 1
    emprestimos.append(emprestimo)
    return emprestimo

@app.delete("/emprestimos/{emprestimo_id}", response_model=Emprestimo)
def excluir_emprestimo(emprestimo_id:int):
    for index, emprestimo in enumerate(emprestimos):
        if emprestimo_id == emprestimo.id:
            del emprestimos[index]
            return emprestimo
    raise HTTPException(status_code=404, detail="Não localizado")
