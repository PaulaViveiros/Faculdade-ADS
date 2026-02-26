distancia = float(input('Qual é a distância da sua viagem em km? '))   
print(f'Você está prestes a começar uma viagem de {distancia} km.')

# Essa sua linha de baixo está LINDA! É um IF simplificado (Ternário)
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print(f'E o preço da sua passagem será de R$ {preço:.2f}')