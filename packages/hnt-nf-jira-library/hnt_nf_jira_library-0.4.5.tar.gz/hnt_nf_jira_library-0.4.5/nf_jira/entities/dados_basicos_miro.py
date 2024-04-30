from pydantic import BaseModel

class DadosBasicosMiro(BaseModel):
    data_da_fatura: str
    referencia: str
    montante: float
    texto: str