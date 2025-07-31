from garrafas_solver import encontrar_melhor_combinacao

# Entrada do volume do galão
galao = float(input("Insira o volume do galão: "))

# Entrada da quantidade de garrafas
quantidade_garrafas = int(input("Quantidade de garrafas: "))

# Lista para armazenar os volumes das garrafas
garrafas = []
for i in range(quantidade_garrafas):
    volume = float(input(f"Garrafa {i+1}:\n"))
    garrafas.append(volume)

# Chamada da função
melhor_combinacao, menor_sobra = encontrar_melhor_combinacao(galao, garrafas)

# Exibe a melhor combinação encontrada
garrafas_str = [f"{int(v) if v.is_integer() else v}L" for v in melhor_combinacao]
sobra_str = f"{int(menor_sobra) if menor_sobra.is_integer() else menor_sobra}L"
print(f"Resposta: [{', '.join(garrafas_str)}], sobra {sobra_str}")
