# 38. Em uma eleição presidencial existem quatro
# candidatos. Os votos são informados através de
# códigos. Os dados utilizados para a contagem dos
# votos obedecem à seguinte codificação:
# 1,2,3,4 = voto para os respectivos candidatos;
# 5 = voto nulo;
# 6 = voto em branco;
# Elabore um algoritmo que leia o código do candidato
# em um voto. Calcule e escreva as seguintes
# informações:
# a) total de votos para cada candidato;
# b) total de votos nulos;
# c) total de votos em branco;
# Como finalizador do conjunto de votos, utilize o valor 0.

voto_nulo = 0
voto_branco = 0
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
marcador = 1



while marcador > 0:
    voto = int(input("Escolha, voto de candidatos (1,2,3,4), vote nulo (5) ou vote em branco(6): "))
    if voto == 1:
        candidato1 = candidato1 + 1
    else:
        if voto == 2:
            candidato2 = candidato2 + 1
        else:
            if voto == 3:
                candidato3 = candidato3 + 1
            else:
                if voto == 4:
                    candidato4 = candidato4 + 1
                else:
                    if voto == 5:
                        voto_nulo = voto_nulo + 1
                    else:
                        if voto == 6:
                            voto_branco = voto_branco + 1
                        else:
                            if voto == 0:
                                marcador = 0
                            else:
                                print("voto inválido")







print(f"número de votos - I-candidato  = {candidato1}, II-candidato  = {candidato2}, III-candidato  = {candidato3}, IV-candidato  = {candidato4}, votos em branco = {voto_branco}, votos nulos = {voto_nulo}.")