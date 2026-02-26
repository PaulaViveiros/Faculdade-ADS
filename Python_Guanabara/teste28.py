#O from é apenas a palavra que a gente usa para dizer "Dessa biblioteca aqui, eu quero só isso...".
#random é a biblioteca que tem várias funções relacionadas a números aleatórios.
#randint é a função que gera números inteiros aleatórios.
#time é a biblioteca que tem várias funções relacionadas a tempo.
#sleep é a função que "pausa" o programa por um tempo determinado.

from random import randint 
from time import sleep
computador = randint(0, 10) # Faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? De 0 a 10: ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!') 


