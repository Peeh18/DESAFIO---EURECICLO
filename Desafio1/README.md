# Desafio 1 - API de Upload e Processamento de Artigos

Este projeto é uma API desenvolvida em FastAPI para upload de arquivos `.zip` contendo artigos em XML, extração, processamento e publicação de mensagens via RabbitMQ.

## Funcionalidades

- Upload de arquivos `.zip` contendo artigos em XML.
- Extração e parsing dos arquivos XML.
- Armazenamento temporário dos artigos extraídos.
- Publicação dos artigos processados em uma fila RabbitMQ.
- Listagem dos artigos extraídos via endpoint.

## Como executar localmente

1. **Pré-requisitos**:
   - Python 3.11+
   - Docker e Docker Compose

2. **Instalação das dependências**:
   ```bash
   pip install fastapi uvicorn pika python-multipart lxml
   ```

3. **Executando a API**:
   ```bash
   uvicorn app.main:app --reload
   ```
   Acesse em: [http://localhost:8000/docs](http://localhost:8000/docs)

## Como executar com Docker Compose

1. Construa e suba os serviços:
   ```bash
   docker-compose up --build
   ```
2. Acesse a API em [http://localhost:8000/docs](http://localhost:8000/docs)
3. O painel do RabbitMQ estará disponível em [http://localhost:15672](http://localhost:15672) (usuário/senha padrão: guest/guest)

## Testes

Os testes unitários estão na pasta `tests/` e podem ser executados com:
```bash
pytest
```

## Estrutura do Projeto

- `app/` - Código principal da aplicação
  - `main.py` - Inicialização da API FastAPI
  - `routes/` - Rotas da API (upload, listagem)
  - `services/` - Serviços de extração e parsing
  - `messaging/` - Publicação de mensagens RabbitMQ
  - `models/` - Modelos de dados (Pydantic)
  - `storage.py` - Armazenamento temporário dos artigos
- `tests/` - Testes unitários
- `Dockerfile` e `docker-compose.yml` - Para execução em containers

## Autor

Pedro Henrique

---
