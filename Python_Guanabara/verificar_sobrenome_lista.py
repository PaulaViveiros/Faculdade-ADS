nome = str(input('Qual é o seu nome completo? ')).strip()
separa = nome.upper().split()
tem_silva = 'SILVA' in separa
print(f'Seu nome tem o sobrenome Silva? {tem_silva}')