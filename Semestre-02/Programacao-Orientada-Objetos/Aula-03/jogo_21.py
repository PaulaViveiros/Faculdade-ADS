print("---BEM-VINDO AO JOGO 21 --- ")

soma = 0
jogar = 's'

while soma < 21 and jogar == 's':
    carta = int(input("Digite o valor da carta: "))
    soma += carta

    if soma < 21:
        print(f'Sua soma atual é {soma}.')
        jogar = input("Deseja pegar mais uma carta? (s/n): ").lower()
     
print("----------------------------------------------")

if soma == 21:
   print("Parabéns! Você ganhou!")
elif soma > 21:
   print(f'ESTOUROU! Sua soma é {soma}. Você perdeu!')
else:
    print(f'Você parou estrategicamente com a soma de {soma} de pontos.')
print("----------------FIM DE JOGO-------------------")