'''cidade = str(input('Em qual cidade você nasceu?')).strip()
print(cidade[:5].upper() == 'SANTO')  '''

cidade = str(input('Em qual cidade você nasceu?')).strip()
separa = cidade.split()
print(separa[0].upper() == 'SANTO')