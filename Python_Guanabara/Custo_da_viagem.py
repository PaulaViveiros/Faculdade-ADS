distancia = float(input('Qual é a distância da sua viagem em km? '))

if distancia <= 0:
    print('❌ Distância inválida! Por favor, digite um valor maior que zero.')
else:
    preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
    print(f'Você está prestes a começar uma viagem de {distancia:.0f}km.')
    print(f'O preço da sua passagem será de R$ {preço:.2f}')