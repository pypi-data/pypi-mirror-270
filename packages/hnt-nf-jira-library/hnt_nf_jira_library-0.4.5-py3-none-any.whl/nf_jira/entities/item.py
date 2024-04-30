from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    centro: str
    centro_custo: str
    cod_imposto: str
    valor_bruto: float
    valor_liquido: Optional[float]=0.0
    percentage: float