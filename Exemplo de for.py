inicio = int(input("Digite um valor de início: "))
final = int(input("Digite um valor de término: "))
incremento = int(input("Digite o incremento: "))
for contador in range(inicio, final + 1, incremento):
    print(contador)
