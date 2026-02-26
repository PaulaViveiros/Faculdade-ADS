'''salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário * 1.15
else:
    novo = salário * 1.10
print(f'Quem ganhava R${salário:.2f} passa a ganhar R${novo:.2f} agora.')'''

salário = float(input('Qual é o salário do funcionário? R$'))

if salário <= 1250:
    novo = salário * 1.15
    porcentagem = 15  
else:
    novo = salário * 1.10
    porcentagem = 10  

# Agora usamos a nova variável no print
print(f'Com um aumento de {porcentagem}%, quem ganhava R${salário:.2f} passa a ganhar R${novo:.2f} agora.')
