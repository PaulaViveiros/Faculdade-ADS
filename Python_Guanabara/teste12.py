preço = float(input('Preço do produto: R$' ))
novo_preço = preço - (preço * 5 /100)
print(f'O produto que custava R$ {preço:.2f}, na promoção com desconto de 5%, vai custar R$ {novo_preço:.2f}')
