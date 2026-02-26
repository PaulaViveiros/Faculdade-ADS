'''nome = str(input('Digite seu nome: '))
print('Analisando seu nome...')
print(f'Seu nome em maiúscula é {nome.upper()}')
print(f'Seu nome em minúscula é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} Letras')
#print(f'Seu primeiro nome é {nome.find(" ")} Letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} Letras')'''

'''quadrinho = str(input('Digite o nome do seu quadrinho favorito: ')).strip()
primeiro_nome = quadrinho.split()[0]
print(f'O primeiro nome do seu quadrinho favorito é {quadrinho.split()[0]} e ele tem {len(quadrinho.split()[0])} letras.')'''

'''quadrinho = str(input('Digite o nome do seu quadrinho favorito: ')).strip()
# Verificamos se o usuário não deixou o campo vazio para não dar erro no split
if quadrinho:
    primeiro_nome = quadrinho.split()[0]
    print(f'O primeiro nome do seu quadrinho favorito é {primeiro_nome} e ele tem {len(primeiro_nome)} letras.')
else:
    print('Você não digitou nenhum nome!')'''

'''quadrinho = str(input('Digite o nome do seu quadrinho favorito: ')).strip()

if quadrinho:
    # Dividimos e pegamos o primeiro nome
    primeiro_nome = quadrinho.split()[0]
    
    # Usamos o capitalize() para formatar a primeira letra
    nome_formatado = primeiro_nome.capitalize()
    
    print(f'O primeiro nome é {nome_formatado} e ele tem {len(nome_formatado)} letras.')''' 

'''quadrinho = str(input('Digite o nome do seu quadrinho favorito: ')).strip()

if quadrinho:
    # Pegamos o primeiro nome e já formatamos com title()
    # Assim, 'x-men' vira 'X-Men' e 'superman' vira 'Superman'
    primeiro_nome = quadrinho.split()[0].title()
    
    print(f'O primeiro nome é {primeiro_nome} e tem {len(primeiro_nome)} letras.')'''

'''# 1. Pegamos o nome, limpamos os espaços (strip) e já deixamos os títulos bonitos (title)
quadrinho = str(input('Digite o nome do seu quadrinho favorito: ')).strip().title()

if quadrinho:
    # 2. Contamos o tamanho total (incluindo espaços entre as palavras)
    tamanho = len(quadrinho)
    
    print(f'O seu quadrinho favorito é "{quadrinho}" e o nome completo tem {tamanho} caracteres.')'''

'''quadrinho = str(input('Digite o nome do seu quadrinho favorito: ')).strip().title()

if quadrinho:
    # O replace(' ', '') troca o espaço ' ' por nada ''
    so_letras = quadrinho.replace(' ', '')
    
    quantidade = len(so_letras)
    
    print(f'O seu quadrinho favorito é "{quadrinho}".')
    print(f'Ele tem {quantidade} letras (sem contar os espaços).')'''