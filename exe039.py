from datetime import date

ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))

if idade > 18:
    atraso = idade - 18
    ano2 = atual - atraso
    print('Voçê deveria ter se alistado há {} anos\nSeu alistamento foi em {}. '.format(atraso, ano2))
elif idade == 18:
    print('Voçê tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    adiantado = 18 - idade
    ano3 = atual + adiantado
    print('Ainda faltam {} anos para seu alistamento\nSeu alistamento será em {}'.format(adiantado, ano3))
