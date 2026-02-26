casa = float(input('Digite o valor da casa: R$ '))
salário = float(input('Digite o seu salário: R$ '))
anos = int(input('Em quantos anos você pretende pagar? '))
prestação = casa / (anos * 12)
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos, a prestação será de R$ {prestação:.2f} mensais.')


