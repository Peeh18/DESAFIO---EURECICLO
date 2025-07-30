# garrafas.py

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


print(f"\nGalão: {galao}L")
print(f"Garrafas: {garrafas}")
