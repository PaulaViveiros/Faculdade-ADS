'''import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print(f'O ângulo de {angulo} tem o Seno de {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O ângulo de {angulo} tem o Cosseno de {cosseno:.2f}')
tangente =  math.tan(math.radians(angulo))
print(f' O ângulo de {angulo} tem a Tangente de {tangente:.2f}')'''

from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o Seno de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o Cosseno de {cosseno:.2f}')
tangente =  tan(radians(angulo))            
print(f' O ângulo de {angulo} tem a Tangente de {tangente:.2f}')


