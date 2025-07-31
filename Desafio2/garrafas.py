# garrafas.py
from itertools import combinations

# Entrada do volume do galão
galao = float(input("Insira o volume do galão: "))

# Entrada da quantidade de garrafas
quantidade_garrafas = int(input("Quantidade de garrafas: "))

# Lista para armazenar os volumes das garrafas
garrafas = []

# Loop que vai receber a entrada de cada garrafa
for i in range(quantidade_garrafas):
    volume = float(input(f"Garrafa {i+1}:\n"))
    garrafas.append(volume)

# Variáveis para armazenar a melhor combinação
melhor_combinacao, menor_sobra = encontrar_melhor_combinacao(galao, garrafas)

# Verifica todas as combinações possíveis de garrafas
for r in range(1, quantidade_garrafas + 1):
    for combinacao in combinations(garrafas, r):
        soma = sum(combinacao)
        sobra = soma - galao
        
        if sobra >= 0:
            if (menor_sobra is None or sobra < menor_sobra) or \
               (sobra == menor_sobra and len(combinacao) < menor_quantidade):
                melhor_combinacao = combinacao
                menor_sobra = sobra
                menor_quantidade = len(combinacao)


# Exibe a melhor combinação encontrada
garrafas_str = [f"{int(v) if v.is_integer() else v}L" for v in melhor_combinacao]
sobra_str = f"{int(menor_sobra) if menor_sobra.is_integer() else menor_sobra}L"
print(f"Resposta: [{', '.join(garrafas_str)}], sobra {sobra_str}")
