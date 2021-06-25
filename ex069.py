#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa 
#cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
tot18 = totH = totM20 = 0
while True:
    age = int(input('Idade: '))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if age >= 18:
        tot18 += 1
    if gender == "M":
        totH += 1
    if gender == 'F' and age < 20:
        totM20 += 1
    answer = ' '
    while answer not in 'SN':
        answer = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if answer == 'N':
        break
print(f'Total de pessoas com mais de 18 anos:{tot18}.')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres de 20 anos.')



