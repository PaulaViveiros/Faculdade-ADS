from codigo.jogo import verificar_idade

try:
    entrada = int(input("Digite sua idade: "))
    print(verificar_idade(entrada))
except ValueError as e:
    print(f"Ops, erro de digitacao: {e}")