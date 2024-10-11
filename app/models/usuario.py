from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.connection import db

# Criando tabela.
Base = declarative_base()

class Usuario(Base):
    # Definindo nome da tabela.
    __tablename__ = "usuarios"

    # Definindo atributos da tabela.
    id = Column(Integer, primary_key= True, autoincrement= True)
    nome = Column(String(250))
    email = Column(String(250), unique= True)
    senha = Column(String(250))

    # Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind = db)