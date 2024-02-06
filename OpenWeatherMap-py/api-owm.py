import requests
import json
import datetime
from time import sleep

def line():
    print('')

exit = False
i = 0
while not exit:
    continuar = ' '
    cidade = str(input('Digite o nome da cidade: '))
    sleep(1)
    line()
    print('loading...',flush=True)
    line()
    requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cidade +
                                '&appid=04709bab937b27275f2b1d2430536d3a')
    response = json.loads(requisicao.text)

    try:
        print('Condição do tempo:', response['weather'][0]['main'])
        print(f'A temperatura de {cidade} está:', (response['main']['temp'] - 273.15))
        i += 1
        cookie = datetime.datetime.now()
        print(f'ultimo acesso: {cookie}')

    except Exception as e:
        print(f'aconteceu um erro>> {e}')
    while continuar not in 'SN':
        line()
        continuar = str(input('Quer continuar [S/N]')).upper()
        line()
    if continuar == 'N':
        exit = True  
print(f'Você pesquisou {i}x api-OpenWeatherMap :)')