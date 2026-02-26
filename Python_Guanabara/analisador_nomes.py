
nome_quadrinho = str(input('Digite o nome do seu quadrinho favorito: ')).strip()

print('\n--- ANALISANDO O NOME ---')

print(f'Em MAIÚSCULAS: {nome_quadrinho.upper()}')
print(f'Em minúsculas: {nome_quadrinho.lower()}')
print(f'Formato de Título: {nome_quadrinho.title()}')

total_letras = len(nome_quadrinho) - nome_quadrinho.count(' ')
print(f'O nome tem ao todo {total_letras} letras (sem contar espaços).')

separa = nome_quadrinho.split()

if len(separa) > 0:
    primeiro_nome = separa[0].title()
    print(f'O primeiro nome é "{primeiro_nome}" e ele tem {len(separa[0])} letras.')