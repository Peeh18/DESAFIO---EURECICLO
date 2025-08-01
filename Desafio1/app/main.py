# app/main.py

# Importa o FastAPI (o "motor" da API)
from fastapi import FastAPI

# Importa o router que você criou no upload.py
from app.routes.upload import router as upload_router

# Cria a instância da API (FastAPI)
app = FastAPI()

# Adiciona a rota de upload dentro da aplicação
app.include_router(upload_router)