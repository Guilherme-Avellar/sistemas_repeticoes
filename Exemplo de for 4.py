meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro' ]

mes = int(input("Digite o número do mês: "))

print(meses[mes-1])


# tem o [mes - 1] no print, pq o vetor começa do zero... mas os meses começam no 1. então se por 11, ele da dezembro,
# então se faz esse ajuste no print