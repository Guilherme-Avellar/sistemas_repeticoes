# 50. Escrever um algoritmo que leia um valor N inteiro e
# positivo e que calcula o valor de E. Imprime o resultado
# de E ao final.
# E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / N!

# n = int(input("Digite um número: "))
# contador = n
#
# while contador != 1:
#     contador = contador - 1
#     n = n * contador
# E = 1 + 1 / 1 + 1 / (2 * 1) + 1 / (3 * 2) + 1 / n
# print(f"N! = {n}")
# print(f"valor de E = {E:.2f}")


# marco, é o certo mermo
valor = int(input("Digite um valor: "))
if valor <= 0:
    print("Valor deve ser inteiro e positivo")
else:
    e = 1
    for i in range(1, valor + 1):
        fat = 1
        for j in range(1, i + 1):
            fat = fat * j

        e = e + (1 / fat)


print(f"E = {e:.2f}")