carro_alugado = int(input('Quantos dias o carro foi alugado? '))
km_percorridos = float(input('Quantos km foram percorridos? '))     
preço_dias = carro_alugado * 60
preço_km = km_percorridos * 0.15
preço_total = preço_dias + preço_km
print(f'O total a pagar é de R$ {preço_total:.2f}')     