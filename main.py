from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Categoria, Produto # Importando seus novos modelos

app = FastAPI(title="Gestão de Produtos")
templates = Jinja2Templates(directory="templates")

# --- ROTAS DE CATEGORIAS ---

@app.get("/categorias/cadastro", response_class=HTMLResponse)
def exibir_cadastro_categoria(request: Request):
    return templates.TemplateResponse("cadastro_categoria.html", {"request": request})

@app.post("/categorias")
def criar_categoria(
    nome: str = Form(...),
    descricao: str = Form(None),
    db: Session = Depends(get_db)
):
    nova_categoria = Categoria(nome=nome, descricao=descricao)
    db.add(nova_categoria)
    db.commit()
    return RedirectResponse(url="/listar_categorias", status_code=303)

@app.get("/listar_categorias", response_class=HTMLResponse)
def listar_categorias(request: Request, db: Session = Depends(get_db)):
    categorias = db.query(Categoria).all()
    return templates.TemplateResponse(
        "categorias.html", 
        {"request": request, "categorias": categorias}
    )

# --- ROTAS DE PRODUTOS ---

@app.get("/produtos/cadastro", response_class=HTMLResponse)
def exibir_cadastro_produto(request: Request, db: Session = Depends(get_db)):
    # Buscamos as categorias para preencher um <select> no formulário
    categorias = db.query(Categoria).all()
    return templates.TemplateResponse(
        "cadastro_produto.html", 
        {"request": request, "categorias": categorias}
    )

@app.post("/produtos")
def criar_produto(
    nome: str = Form(...),
    preco: float = Form(...),
    estoque: int = Form(...),
    categoria_id: int = Form(...),
    db: Session = Depends(get_db)
):
    novo_produto = Produto(
        nome=nome, 
        preco=preco, 
        estoque=estoque, 
        categoria_id=categoria_id
    )
    db.add(novo_produto)
    db.commit()
    return RedirectResponse(url="/listar_produtos", status_code=303)


#Listar

@app.get("/listar_produtos", response_class=HTMLResponse)
def listar_produtos(request: Request, db: Session = Depends(get_db)):
    produtos = db.query(Produto).all()
    return templates.TemplateResponse(
        "produtos.html", 
        {"request": request, "produtos": produtos}
    )

#Deletar

@app.post("/produtos/{id}/deletar")
def deletar_produto(id: int, db: Session = Depends(get_db)):
    # .first() é essencial para pegar a instância do objeto
    produto = db.query(Produto).filter(Produto.id == id).first()
    if produto:
        db.delete(produto)
        db.commit()
    return RedirectResponse(url="/listar_produtos", status_code=303)