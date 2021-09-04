# 37. Construir um algoritmo que calcule a média aritmética
# de vários valores inteiros positivos, digitados pelo
# usuário. O final da leitura acontecerá quando for lido
# um valor negativo.

# melhor solução
soma_valor = 0
qtde_valores = 0
valor = int(input("Digite um valor: "))
while valor >= 0:
    soma_valor = soma_valor + valor
    qtde_valores = qtde_valores + 1
    valor = int(input("Digite um valor: "))

if qtde_valores > 0:
    print(f"Média = {soma_valor / qtde_valores:.2f}")

# minha solução

contador = 0
soma = 0
numero = 0

while numero >= 0:
    numero = int(input(f"Digite um número {contador + 1}: "))
    if numero >= 0:
        soma = soma + numero
        contador = contador + 1

if contador > 0:
    print(f"A média dos números digitados é {soma / contador:.2f}")

