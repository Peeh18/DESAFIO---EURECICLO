## Desafio Eureciclo - Combinação de Garrafas

Este projeto resolve o problema de encontrar a melhor combinação de garrafas para preencher um galão, minimizando a sobra.

### Como executar localmente

1. Certifique-se de ter o Python 3 instalado.
2. Instale as dependências (se houver):
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script:
   ```bash
   python garrafas.py
   ```

### Como executar via Docker

1. Construa a imagem Docker:
   ```bash
   docker build -t desafio-garrafas .
   ```
2. Execute o container:
   ```bash
   docker run -it desafio-garrafas
   ```

### Testes

Os testes unitários podem ser executados com:
```bash
pytest
```

### Pipeline CI

O projeto inclui um pipeline para execução dos testes e análise estática. A cada push, os testes e o lint são executados automaticamente.

---
Autor: Pedro Henrique
