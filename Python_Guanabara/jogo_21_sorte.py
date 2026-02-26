import random

print("--- Bem-vindo ao Jogo 21 da sorte ---")

soma = 0
jogar = 's'

while soma < 21 and jogar == 's':
    input('Pressione Enter para tirar uma carta...')

    carta = random.randint(1, 10)
    soma += carta

    print(f'Você tirou a carta: {carta}')
    print(f'Sua soma atual é {soma}.')

    if soma < 21:
        jogar = input('Deseja arriscar mais uma carta? (s/n)> ').lower()
print('----------------------------------------------')
if soma == 21:
    print('Parabéns você atingiu 21 e ganhou!')
elif soma > 21:
    print(f'ESTOUROU! {soma} pontos. Você perdeu')
else:
    print(f'Você parou com a {soma} de pontos. Boa estratégia!')

print('------------------ FIM DE JOGO ------------------')
