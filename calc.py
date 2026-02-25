# Programa para calcular a média de 4 números

# 1. Definindo os 4 números
num1 = 7.5
num2 = 8.0
num3 = 6.5
num4 = 9.0

# 2. (Já estão como float, mas mantemos a lógica)
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
num4 = float(num4)

# 3. Calcula a média
media = (num1 + num2 + num3 + num4) / 4

# 4. Exibe o resultado com duas casas decimais
print(f"A média é: {media:.2f}")
