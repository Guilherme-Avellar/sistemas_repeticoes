# 39. Escrever um algoritmo que leia uma variável n e calcule
# a tabuada de 1 até n. Mostre a tabuada na forma:
# 1 x n = n
# 2 x n = 2n
# 3 x n = 3n
# ...............
# n x n = n2

# minha

n = float(input("Digite um número, para sua tabuada: "))
contador = 0


while n * n > contador * n:
    contador = contador + 1
    print(f"{contador} x {n} = {contador * n}")


# marco

numero = int(input("Digite um numero: "))
contador = 1
while contador <= numero:
    print (f"{contador} x {numero} = {contador * numero}")
    contador = contador + 1

