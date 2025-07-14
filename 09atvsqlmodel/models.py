from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Pedido(SQLModel, table=True):
    IdPedido: int = Field(primary_key=True)
    ProtocoloPedido: str
    Esfera: str
    UF: Optional[str] = None
    Municipio: Optional[str] = None
    OrgaoDestinatario: str
    Situacao: str
    DataRegistro: date
    PrazoAtendimento: date
    FoiProrrogado: str
    FoiReencaminhado: str
    FormaResposta: Optional[str] = None
    OrigemSolicitacao: str
    IdSolicitante: int
    AssuntoPedido: str
    SubAssuntoPedido: str
    Tag: Optional[str] = None
    DataResposta: Optional[date] = None
    Decisao: Optional[str] = None
    EspecificacaoDecisao: Optional[str] = None
