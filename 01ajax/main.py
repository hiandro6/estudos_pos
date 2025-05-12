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

usuarios: List[Usuario] = []
livros: List[Livro] = []
bibliotecas: List[Biblioteca] = []
emprestimos: List[Emprestimo] = []


# usuários:
@app.get("/usuarios/{biblioteca}", response_model=List[Usuario])
def listar_usuarios(biblioteca:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == biblioteca:
            return usuarios
    raise HTTPException(status_code=404, detail="Não localizada")
    

@app.get("/usuarios/{biblioteca}/{username}", response_model=Usuario)
def listar_usuario(username:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == biblioteca:
            for usuario in usuarios:
                if usuario.username == username:
                    return usuario
            raise HTTPException(404, "Usuário não localizado")

@app.post("/usuarios/", response_model=Usuario)
def criar_usuario(usuario:Usuario):
    usuario.id = len(usuarios) + 1
    usuarios.append(usuario)
    return usuario

@app.delete("/usuarios/{username}", response_model=Usuario)
def excluir_usuario(username:str):
    for index, usuario in enumerate(usuarios):
        if username == usuario.username:
            del usuarios[index]
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não localizado")














# biblioteca: 
@app.get("/biblioteca/", response_model=List[Biblioteca])
def listar_bibliotecas():
    return bibliotecas


@app.get("/biblioteca/{nome}", response_model=Biblioteca)
def listar_bibliotecas(nome:str):
    for lib in bibliotecas:
        if lib.nome == nome:
            return lib
    raise HTTPException(status_code=404, detail="Não localizada")

@app.post("/biblioteca/", response_model=Biblioteca)
def criar_biblioteca(nome:str):
    lib_id = len(bibliotecas) + 1
    data = {
        "id": lib_id,
        "nome": nome,
        "acervo": [],
        "usuarios": [],
        "emprestimos": []
    }


    biblioteca = Biblioteca(**data)
    # biblioteca.id = len(bibliotecas) + 1
    # biblioteca.nome = nome
    # biblioteca.acervo = []
    # biblioteca.usuarios = []
    # biblioteca.emprestimos = []

    bibliotecas.append(biblioteca)
    return biblioteca

@app.delete("/biblioteca/{nome}", response_model=Biblioteca)
def excluir_biblioteca(nome:str):
    for index, biblioteca in enumerate(bibliotecas):
        if nome == biblioteca.nome:
            del bibliotecas[index]
            return biblioteca
    raise HTTPException(status_code=404, detail="Não localizado")









# livros:
@app.get("/livros/", response_model=List[Livro])
def listar_livros():
    return livros

@app.get("/livros/{titulo}", response_model=Livro)
def listar_livro(titulo:str):
    for livro in livros:
        if livro.titulo == titulo:
            return livro
        
    raise HTTPException(404, "livro não encontrado")

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

@app.delete("/livros/{titulo}", response_model=Livro)
def excluir_livro(titulo:str):
    for index, livro in enumerate(livros):
        if titulo == livro.titulo:
            del livros[index]
            return livro
    raise HTTPException(status_code=404, detail="Não localizado")






# empréstimmos: 
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
