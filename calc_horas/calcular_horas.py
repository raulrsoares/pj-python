import os

# Linux
os.system('clear')
# Windows
os.system('cls')
print('=========================== Conversor de horas ===========================')
horas = (input('Quantas horas no dia: '))
dias = (input('Quantos dias foram? '))

# Converter horas
conver = float(horas) * 60
horasTotais = int(conver) * int(dias)

# Quantidade de Horas
horaGerais = int(horasTotais) / 60 

print(f'Você tem {horasTotais} minutos, ou seja {horaGerais} horas!')
