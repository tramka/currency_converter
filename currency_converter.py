import requests
import argparse
import json
import sys
from config import currencies, defaults

allowed_currencies = sorted({x for item in currencies.items() for x in item})


def positive_value(num):
    """
    Checks whether num is positive number and returns it in float format.

    Parameters
    ----------
    num : str
        Amount of money.

    Returns
    -------
    float
        Amount of money in float format.
    """

    try:
        value = float(num)
        if value < 0:
            msg = "{} is not positive number.".format(num)
            raise argparse.ArgumentTypeError(msg)
        return value
    except ValueError:
        raise argparse.ArgumentTypeError('"{}" is not number.'.format(num))


def check_currency(currency):
    """
    Checks provided currency and returns its three letter code. If currency is
    a symbol, value is transformed to 3-letter code. In case that symbol is
    used in more countries, default value is returned according to countries'
    population).

    Parameters
    ----------
    currency : str
        Currency in 3-letter format or as symbol.

    Returns
    -------
    str
        3-letter format of currency.
    """

    if currency in currencies.values():

        if currency in defaults:
            currency = defaults[currency]

        else:
            currency = {v: k for k, v in currencies.items()}[currency]

    return currency


def parser():
    """
    Function parses provided inputs from user while executing script.

    Returns
    -------
    dict
        Payload of user's input.
	"""

    parser = argparse.ArgumentParser(description="Currency converter.")
    parser.add_argument(
        "--amount",
        help="amount of money to be converted",
        type=positive_value,
        required=True,
    )
    parser.add_argument(
        "--input_currency",
        help="input currency",
        required=True,
        type=check_currency,
        choices=allowed_currencies,
    )
    parser.add_argument(
        "--output_currency",
        help="output_currency",
        type=check_currency,
        choices=allowed_currencies,
    )

    args = parser.parse_args()
    return vars(args)


def get_currency_rates(base):
    """
    Downloads data for selected base currency from ExchangeRatesAPI.

    Parameters
    ----------
    base : str
        Currency code in 3-letter code format or as symbol.

    Returns
    -------
    dict
        Conversion rates for selected bsae currency.
    """

    URL = "https://api.exchangeratesapi.io/latest?base={}".format(base)

    try:
        response = requests.get(URL)
        response.raise_for_status()
        return response.json()["rates"]
    except requests.exceptions.HTTPError as err:
        print("Http Error: ", err)
    except requests.exceptions.ConnectionError as errc:
        print("Connection Error: ", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error: ", errt)
    except requests.exceptions.RequestException as e:
        print("Oops: ", e)


def conversion(amount, rates, output_currency=None):
    """
    Converts amount from input currency to the output currency. If output
    currency is not defined, conversion is made for all supported currencies.

    Parameters
    ----------
    amount : float
        Amount of money to be converted.
    rates : dict
        Conversion rates.
    output_currency : str, optional
        Currency for which conversion is made.

    Returns
    -------
    dict
        Converted rates.
    """

    result = {
        k: round(v * amount, 2) for k, v in rates.items()
    }  # it is necessary to have float(amount)?

    if output_currency:
        result = {output_currency: result[output_currency]}

    return result


def get_results(amount, input_currency, converted_data):
    """
    Loads transformed data to the dictionary.

    Parameters
    ----------
    amount : float
        Amount of money.
    input_currency : str
        Currency in 3-letter format.
    converted_data : dict
        Converted rates.

    Returns
    -------
    dict
        Final results.
    """

    final_data = {"input": {"amount": None, "currency": None}, "output": {}}

    final_data["input"].update(amount=amount, currency=input_currency)
    final_data.update(output=converted_data)

    return final_data

def main(payload):
    """
	Orchestrates the whole application to make conversion from one currency
    to another.

    Parameters
    ----------
    payload : dict
        Inputs entered by user - contains amount, input currency and optionally
        output currency.

    Returns
    -------
    dict
        Final results.
    """

    amount = payload["amount"]
    base = payload["input_currency"]
    output_currency = payload["output_currency"]

    raw_data = get_currency_rates(base)
    if not raw_data:
        sys.exit(1)

    converted_data = conversion(amount, raw_data, output_currency=output_currency)
    final_data = get_results(amount, base, converted_data)

    with open("result.json", "w") as fp:
        json.dump(final_data, fp)
    return final_data


if __name__ == "__main__":

    payload = parser()
    result = main(payload)
    print(json.dumps(result, indent=4, sort_keys=True))
