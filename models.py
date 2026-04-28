from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(150))

    # 1. Mudamos 'alunos' para 'produtos' (faz mais sentido aqui)
    # 2. back_populates deve apontar para o nome do atributo na classe Produto (que é 'categoria')
    produtos = relationship("Produto", back_populates="categoria")

    def __repr__(self):
        return f"<Categoria(id={self.id}, nome='{self.nome}')>"

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)

    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    # 3. back_populates deve apontar para o nome do atributo na classe Categoria (que agora é 'produtos')
    categoria = relationship("Categoria", back_populates="produtos")

    def __repr__(self):
        # 4. Corrigido de 'self.categorias.nome' para 'self.categoria.nome' (singular)
        return f"<Produto(id={self.id}, nome='{self.nome}', categoria='{self.categoria.nome if self.categoria else 'N/A'}')>"
