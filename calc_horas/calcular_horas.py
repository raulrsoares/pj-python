import os

# Linux
os.system('clear')
# Windows
os.system('cls')
print('=========================== Conversor de horas ===========================')
horas = (input('Quantas horas no dia: '))
dias = (input('Quantos dias foram? '))

# Converter horas
conver = float(horas) * int(dias)
horasTotais = int(conver) * 60

print(f'Você tem {horasTotais} minutos, ou seja {conver} horas!')
