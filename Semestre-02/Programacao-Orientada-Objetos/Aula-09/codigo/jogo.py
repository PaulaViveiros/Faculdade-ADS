"""def brincadeira(numero):
    if numero < 3:
        print("Entrei na brincadeira!")
        return numero
    if numero > 4:
        return "goiabada"
    return "queijo"""

def verificar_idade(idade):
    if idade < 0:
        # Aqui o código "GRITA"
        raise ValueError("Idade nao pode ser negativa!")
    return "Idade aceita"