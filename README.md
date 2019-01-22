# Currency Converter

## Description
Application converts amount of money from one currency to another based on values from ExchangeRatesAPI. It is created as CLI application and Web Application.

## Motivation
Application has been created as a task for interview purpose in Kiwi.com.

## Installation
You need Python 3 or later to run currency_converter.

In Ubuntu, Mint or Debian, you can install it by:

``sudo apt-get install python3``

In case you have other distribution, please follow:

https://www.python.org/getit/.

To make script work, create virtual environment and then clone repository. After that, run:
``pip install -r requirements.txt``

### Docker
To run web application, you can use also docker. To build and run a docker, use:

``docker build -t currencies:latest``

``docker run -d -p 5000:5000 currencies:latest``

After that, open the browser and load:

``http://localhost:5000/``

## Usage

### CLI Application

To run the program, use:

``python currency_converter.py --amount [amount] --input_currency [input_currency] --output_currency [output_currency]``

Amount and input_currency are necessary to run application. Output_currency is optional. In case it is not used, conversion is made for all known currencies.

Script creates results in main directory.

Examples:

```json
./currency_converter.py --amount 100.0 --input_currency EUR --output_currency CZK

{
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "CZK": 2558.0
    }
}
```

```json
./currency_converter.py --amount 10.92 --input_currency £
{
    "input": {
        "amount": 10.92,
        "currency": "GBP"
    },
    "output": {
        "AUD": 19.64,
        "BGN": 24.24,
        "BRL": 52.91,
        "CAD": 18.75,
        "CHF": 14.04,
        "CNY": 95.78,
        "CZK": 316.97,
        "DKK": 92.5,
        "EUR": 12.39,
        "GBP": 10.92,
        "HKD": 110.83,
        "HRK": 92.06,
        "HUF": 3941.61,
        "IDR": 200657.62,
        "ILS": 52.21,
        "INR": 1004.79,
        "ISK": 1707.55,
        "JPY": 1546.21,
        "KRW": 15845.37,
        "MXN": 269.01,
        "MYR": 58.27,
        "NOK": 120.47,
        "NZD": 20.87,
        "PHP": 743.28,
        "PLN": 53.2,
        "RON": 58.23,
        "RUB": 937.13,
        "SEK": 127.03,
        "SGD": 19.16,
        "THB": 448.09,
        "TRY": 75.7,
        "USD": 14.13,
        "ZAR": 194.78
    }
}
```

### Web Application

To run the program, use:

``python web_currency_converter.py``

Open the browser and use following links:

``localhost/currency_converter?amount=[value]&input_currency=[currency_code]&output_currency=[currency_code]``

Examples:

```json
GET /currency_converter?amount=0.9&input_currency=¥&output_currency=AUD HTTP/1.1
{
  "input": {
    "amount": 0.9,
    "currency": "JPY"
  },
  "output": {
    "AUD": 0.01
  }
}
```

```json
GET /currency_converter?amount=10.92&input_currency=£ HTTP/1.1
{
  "input": {
    "amount": 10.92,
    "currency": "GBP"
  },
  "output": {
    "AUD": 19.64,
    "BGN": 24.24,
    "BRL": 52.91,
    "CAD": 18.75,
    "CHF": 14.04,
    "CNY": 95.78,
    "CZK": 316.97,
    "DKK": 92.5,
    "EUR": 12.39,
    ...
  }
}
```

## Contributing
Any idea how to improve project is welcomed. You can create issue here or write message to the email.

## Credits
Created by Tomas Cernak.

Email: cernak.tomi@gmail.com

Released: 20.1.2019

## License
MIT License

## To do
Testing
