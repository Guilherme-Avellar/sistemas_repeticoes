# 49. Escrever um algoritmo que gere e escreva os 3
# primeiros números perfeitos. Um número perfeito é
# aquele que é igual a soma dos seus divisores. (Ex.: 6 =
# 1+2+3; 28= 1+2+4+7+14, etc).



num = 1
num_perfeitos = 0

while num_perfeitos < 4:
    num = num + 1
    num_teste = 0
    soma = 0
    while soma <= num:
        num_teste = num_teste + 1
        if num % num_teste == 0:
            soma = soma + num_teste
        if num == soma and num_teste == num / 2:
            num_perfeitos = num_perfeitos + 1
            print(num)

# quantidade = 0
# numero = 1
# while quantidade < 4:
#
#     soma = 0
#     for i in range(1, int(numero/2)+1):
#         if numero % i == 0:
#             soma = soma + i
#
#     if soma == numero:
#         print(numero)
#         quantidade = quantidade + 1
#
#     numero = numero + 1