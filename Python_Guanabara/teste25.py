'''nome = str(input('Qual é o seu nome completo? ')).strip()
print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')'''

nome = str(input('Qual é o seu nome completo? ')).strip()

# Convertemos para maiúsculas antes de separar para a comparação ser justa
separa = nome.upper().split()

# Agora procuramos por 'SILVA' em maiúsculas dentro da lista
tem_silva = 'SILVA' in separa

# O 'f' deve vir antes das aspas!
print(f'Seu nome tem o sobrenome Silva? {tem_silva}')