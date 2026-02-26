velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) *7
    print(f'MULTADO! você excedeu o limite de velocidade que é de 80km/h')
    print(f'Você deve pagar uma multa de R$ {multa:.2f}')
print(f'Tenha um bom dia! Dirija com segurança!')
