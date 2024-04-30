from pydantic import BaseModel
from typing import Optional

class ItensFatura(BaseModel):
    cta_razao: str
    montante: float
    valor_liquido: Optional[float]=0.0
    percentage: float
    loc_negocios: str
    atribuicao: Optional[str]
    texto: str
    centro_custo: str