# Usa imagem base do Python
FROM python:3.11-slim

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos para dentro do container
COPY . .

# Instala pytest caso haja testes
RUN pip install pytest

# Comando padrão: roda o script
CMD ["python", "garrafas.py"]
