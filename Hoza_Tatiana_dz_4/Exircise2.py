import requests

def currency_rates():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    print(response)
    response = response.text
    print(response)
    response = response.split(' ', -1)
    print(type(response))
    response = " ".join(map(str, response))
    print(type(response))
    name = input('введите код валюты: ')
    for name in response:
        value = response[(response.find('<Value>')): response.find('</Valute>')]
        print(value)

print(currency_rates())