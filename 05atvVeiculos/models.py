from pydantic import BaseModel

class Veiculo(BaseModel):
    nome: str
    marca: str
    modelo: str
    placa: str