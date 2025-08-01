# Usa a imagem oficial do Python 3.11, versão leve
FROM python:3.11-slim

# Define a pasta /app dentro do container como pasta principal
WORKDIR /app

# Copia todos os arquivos do seu projeto para dentro do container (pasta /app)
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir fastapi uvicorn pika python-multipart lxml

# Expõe a porta 8000 para acessar a API de fora do container
EXPOSE 8000

# Comando para iniciar a aplicação FastAPI usando uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]