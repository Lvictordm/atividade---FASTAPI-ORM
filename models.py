# models é o arquivo onde fica as classes (tabelas)
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base



#Tabelas categorias e produtos (1:N) 
class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(150))
    
    produtos = relationship("Produto", back_populates="categorias")

   
class Produtos(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(DECIMAL, nullable=False)
    estoque - Column(Integer, nullable=False)
    
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    categoria = relationship("Categoria", back_populates="produtos")