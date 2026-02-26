from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year  # Puxa o ano do relógio do seu PC!

# A lógica do Bissexto:
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO É BISSEXTO!')