import requests
import argparse
from config import currencies, defaults

allowed_currencies = sorted({x for item in currencies.items() for x in item})

def positive_value(string):

    value = float(string)
    if value < 0:
    	msg = '{} is not positive value.'.format(string)
    	raise argparse.ArgumentTypeError(msg)
    return value

def check_currency(currency):

    if currency in currencies.values():

        if currency in defaults:
            currency = defaults[currency]

        else:
            currency = {v:k for k,v in currencies.items()}[currency]

    return currency

def parser():

    parser = argparse.ArgumentParser(description = 'Currency converter.')
    parser.add_argument(
        '--amount',
        help = 'amount of money to be converted',
        type = positive_value,
        required = True)
    parser.add_argument(
        '--input_currency',
        help = 'input currency',
        required = True,
        type = check_currency,
        choices = allowed_currencies)
    parser.add_argument(
        '--output_currency',
        help = 'output_currency',
        type = check_currency,
        choices = allowed_currencies)

    args = parser.parse_args()
    return vars(args)

def get_currency_rates(base):

    URL = 'https://api.exchangeratesapi.io/latest?base={}'.format(base)
    response = requests.get(URL)

    print(response.status_code)
    return response.json()


def main(payload):

	amount = payload['amount']
	base = payload['input_currency']
	output_currency = payload['output_currency']

	raw_data = get_currency_rates(base)

if __name__ == '__main__':

    payload = parser()
    print(payload)
    main(payload)
