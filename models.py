from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base

class Questionario(Base):
    __tablename__ = "questionario"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    datanascto = Column(Integer)
    genero = Column(String)
    escolaridade = Column(String)
    renda_familiar = Column(String)
    regiaoBrasil = Column(String)
    regiaoBrasil = Column(String)
    regiaoBrasil = Column(String)
    regiaoBrasil = Column(String)
    regiaoBrasil = Column(String)
    regiaoBrasil = Column(String)
    regiaoBrasil = Column(String)
    regiaoBrasil = Column(String)
    regiaoBrasil = Column(String)
    orientacaoPolitica = Column(String)
    frequenciaInformaPolitica = Column(String)
    principaisFontesInformacao = Column(String)
    redeSocial = Column(String)
    costumaBuscarInformacoes = Column(String)
    duranteConversaPoliticaAge = Column(String)
    pessoasProximasDesentenderam = Column(String)
    pessoasDesentenderamAgrediram = Column(String)
    precisouCortarContato = Column(String)
    causaComportamentos = Column(String)
    
class Post(Base):
    __tablename__ = "post"
    
    id = Column(Integer, primary_key=True, index=True)
    post = Column(Integer)
    like = Column(String)
    save = Column(String)
    compartilhar = Column(String)
    comentario = Column(String)
    email = Column(String)