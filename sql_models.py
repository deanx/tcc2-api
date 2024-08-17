from pydantic import BaseModel

class QuestionarioCreate(BaseModel):
    id: int
    email: str
    datanascto: str
    genero: str
    escolaridade: str
    renda_familiar: str
    regiaoBrasil: str
    orientacaoPolitica: str
    frequenciaInformaPolitica: str
    principaisFontesInformacao: str
    redeSocial: str
    costumaBuscarInformacoes: str
    duranteConversaPoliticaAge: str
    pessoasProximasDesentenderam: str
    pessoasDesentenderamAgrediram: str
    precisouCortarContato: str
    causaComportamentos: str
    
    class Config:
        orm_mode = True
        
class PostCreate(BaseModel):
    id: int
    post: int
    like: str
    save: str
    compartilhar: str
    comentario: str
    email: str
        
    class Config:
        orm_mode = True