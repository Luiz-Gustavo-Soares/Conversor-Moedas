import PySimpleGUI as sg
from funcoes import buscmoney, infmoney

cod1 = 'BRL'
cod2 = '----'
din1 = '0'
din2 = '0'

sg.theme('Reddit')

nome = {'Dólar Americano': 'USD', 'Dólar Canadense': 'CAD', 'Libra Esterlina': 'GBP', 'Peso Argentino': 'ARS',
        'Bitcoin': 'BTC', 'Litecoin': 'LTC', 'Euro': 'EUR', 'Iene Japonês': 'JPY', 'Franco Suíço': 'CHF',
        'Dólar Australiano': 'AUD', 'Yuan Chinês': 'CNY', 'Novo Shekel Israelense': 'ILS', 'Ethereum': 'ETH',
        'XRP': 'XRP', 'Dogecoin': 'DOGE'}

op = ('Dólar Americano', 'Dólar Canadense', 'Libra Esterlina', 'Peso Argentino', 'Bitcoin', 'Litecoin', 'Euro',
      'Iene Japonês', 'Franco Suíço', 'Dólar Australiano', 'Yuan Chinês', 'Novo Shekel Israelense', 'Ethereum',
      'XRP', 'Dogecoin')

layout = [
    [sg.Text('Moeda:'), sg.Combo(list(op), default_value='Selecione uma moeda', key='inmoney'),
     sg.Text('Valor:'), sg.Input('1.00', size=(15, 1), key='valor')],
    [sg.Button('Converter'), sg.Button('Informação')],
    [sg.Text(cod1, size=(5, 1)), sg.Text(din1, key='din1', size=(30, 1))],
    [sg.Text(cod2, size=(5, 1), key='cod2'), sg.Text(din2, key='din2', size=(30, 1))]
]

janela = sg.Window('Conversor de moedas', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break

    if evento == 'Converter':
        try:
            nmoeda = nome[valores['inmoney']]
            money = buscmoney(nmoeda, valores['valor'])

        except:
            sg.PopupError('Insira os valores corretamente')
        else:
            janela['cod2'].update(money[0])
            janela['din1'].update(money[2])
            janela['din2'].update(money[1])

    if evento == 'Informação':
        try:
            nmoeda = nome[valores['inmoney']]
            inf = infmoney(nmoeda)

        except:
            sg.PopupError('Insira os valores corretamente')
        else:
            sg.Popup('Informações:',
                     f'Minimo = {inf[0]}',
                     f'Maximo = {inf[1]}',
                     f'Compra = {inf[2]}',
                     f'Venda = {inf[3]}',
                     f'Pct Variação = {inf[4]}')
