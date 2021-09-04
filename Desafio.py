# jogo do pedra papel tesoura melhor de 3


print("Jogo do pedra papel ou tesoura")
print("Pedra = 0, Papel = 1, Tesoura = 2")
contadorp = 0
contadorc = 0

while contadorp != 2 and contadorc != 2:
    player = int(input("Joque pedra, papel ou tesoura: "))
    from random import *
    computador = randint(0,2)
    if player < 0 or player > 2:
        print("O jogo feito está escrito errado ou está inválido")
    else:
        if player == computador:
            print("Empate")
        else:
            if (player == 0 and computador == 2) or (player == 1 and computador == 0) or (
                    player == 2 and computador == 1):
                print("Você venceu")
                contadorp = contadorp + 1
            else:
                print("Derrota")
                contadorc = contadorc + 1
        print(f"O computador jogou {computador}")



if contadorc > contadorp:
    print("você perdeu a melhor de 3")
else:
    if contadorp > contadorc:
        print("você ganhou a melhor de 3")