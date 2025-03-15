# EXEMPLO 1

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(f"Exemplo 1: {pares}")

# EXEMPLO 2

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(f"Exemplo 2: {pares}")

# EXEMPLO 3

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(f"Exemplo 3: {quadrado}")

# EXEMPLO 4

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]

print(f"Exemplo 4: {quadrado}")