from random import randint
from time import sleep

computador = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(2)

# 1º Passo: Verificar se o número é válido
if jogador not in range(0, 11):
    print('❌ Ei! Esse número não vale! Você perdeu a chance por não seguir as regras.')

# 2º Passo: Se for válido, verificar se ganhou (usamos o ELIF ou ELSE)
elif jogador == computador:
    print('✅ PARABÉNS! Você conseguiu me vencer!')

# 3º Passo: Se for válido, mas não for igual ao do computador
else:
    print(f'💻 GANHEI! Eu pensei no {computador} e não no {jogador}!')
