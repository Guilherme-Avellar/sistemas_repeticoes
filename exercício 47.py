# 47.	Escreva um algoritmo que lê um valor n inteiro e positivo e que calcula a seguinte soma: 
# S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
# O algoritmo deve escrever cada termo gerado e o valor final de S.

# n = int(input("Digite um número: "))
# if n > 0:
#     soma = 1
#     contador = 1
#
#     while contador != n:
#         contador = contador + 1
#         termo = 1/contador
#         soma = soma + termo
#         print(f"Termo ={termo:.2f}")
#
#     print(f"{soma:.2f}")

# n = int(input("Digite um número: "))
# if n > 0:
#     soma = 0
#     for i in range(1,n+1):
#         termo = 1/i
#         soma = soma + termo
#         print(f"termo = {termo:.2f}")
#     print(f"soma = {soma:.2f}")





numero = int(input("Digite um número: "))
if numero > 0:
     s = 0
     for i in range(1, numero + 1):
         termo = 1 / i
         print(f"Termo = {termo:.2f}")
         s = s + termo

     print(f"S = {s:.2f}")


