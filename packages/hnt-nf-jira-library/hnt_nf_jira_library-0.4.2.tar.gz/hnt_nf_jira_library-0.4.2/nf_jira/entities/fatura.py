from pydantic import BaseModel

from .dados_basicos_fatura import DadosBasicos
from .pagamento import Pagamento
from .jira_info import JiraInfo

class Fatura(BaseModel):
    dados_basicos: DadosBasicos
    pagamento: Pagamento