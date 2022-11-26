# entre 16 e 69 anos
# pesar mais de  50kg
# ter pelo menos 6 horas de sono 

idade = int(input("Qual é a sua idade? "))

if (idade >= 16) and (idade <= 69):
    kg = int(input('Quantos quilos você pesa? '))
    if (kg > 50):
        sono = int(input("Quantas horas de descanso você teve na noite passada? "))
        if (sono > 6):
            print('Você está liberado para realizar doação de sangue')
        else:
            print('Você não descansou o suficiente para realizar a doação de sangue')
    else:
        print('Você está abaixo do peso mínimo para realizar a doação de sangue')
else:
    print('Você não tem a idade necessária para doar sangue.')