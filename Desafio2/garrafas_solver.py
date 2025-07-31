# garrafas_solver.py
from itertools import combinations

def encontrar_melhor_combinacao(galao, garrafas):
    melhor_combinacao = None
    menor_sobra = None
    menor_quantidade = None

    for r in range(1, len(garrafas) + 1):
        for combinacao in combinations(garrafas, r):
            soma = sum(combinacao)
            sobra = soma - galao

            if sobra >= 0:
                if (menor_sobra is None or sobra < menor_sobra) or \
                   (sobra == menor_sobra and len(combinacao) < menor_quantidade):
                    melhor_combinacao = combinacao
                    menor_sobra = sobra
                    menor_quantidade = len(combinacao)

    return list(melhor_combinacao), menor_sobra