# --- ANALISADOR DE QUADRINHOS PRO ---

# 1. Entrada de dados com limpeza de bordas
nome_quadrinho = str(input('Digite o nome do seu quadrinho favorito: ')).strip()

print('\n--- ANALISANDO O NOME ---')

# 2. Formatação de Estilos
print(f'Em MAIÚSCULAS: {nome_quadrinho.upper()}')
print(f'Em minúsculas: {nome_quadrinho.lower()}')
print(f'Formato de Título: {nome_quadrinho.title()}')

# 3. Contagem Matemática (Estilo Guanabara)
# Pegamos o tamanho total e tiramos a contagem de espaços
total_letras = len(nome_quadrinho) - nome_quadrinho.count(' ')
print(f'O nome tem ao todo {total_letras} letras (sem contar espaços).')

# 4. Usando a variável "separa" (Estilo Lista)
separa = nome_quadrinho.split()

# Verificamos se o usuário digitou algo para não dar erro
if len(separa) > 0:
    primeiro_nome = separa[0].title()
    print(f'O primeiro nome é "{primeiro_nome}" e ele tem {len(separa[0])} letras.')