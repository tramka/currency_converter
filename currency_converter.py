import requests

def get_currency_rates(base):

    URL = 'https://api.exchangeratesapi.io/latest?base={}'.format(base)
    response = requests.get(URL)

    print(response.status_code)
    return response.json()


print(get_currency_rates('USD'))
