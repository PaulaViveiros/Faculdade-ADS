cidade = str(input('Em qual cidade você nasceu? ')).strip()
separa = cidade.split()

# Usamos a lógica de lista para pegar a primeira palavra inteira
# Isso evita erros com cidades como "Santos"
resultado = separa[0].upper() == 'SANTO'

print(f'A cidade começa com "Santo"? {resultado}')