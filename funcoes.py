import requests

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacoes = cotacoes.json()


def buscmoney(v1, v2):
    cot = cotacoes[v1]
    v2 = float(v2)
    valor = float(cot['bid'])
    valor = valor * v2
    valor = f'{valor:.2f}'
    v2 = f'{v2:.2f}'
    return cot['code'], valor, v2


def infmoney(v1):
    cot = cotacoes[v1]
    mini = 'R$ '+cot['low']
    maxi = 'R$ '+cot['high']
    comp = 'R$ '+cot['bid']
    vend = 'R$ '+cot['ask']
    pctvar = cot['pctChange']+'%'
    return mini, maxi, comp, vend, pctvar
