from flask import Flask, request, jsonify, render_template
import currency_converter as cuco
from currency_converter import check_currency

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/currency_converter',methods=['GET'])
def currency_converter():

    amount = request.args.get('amount')
    input_currency = request.args.get('input_currency')
    output_currency = request.args.get('output_currency')

    payload = {'amount': amount,
    'input_currency': check_currency(input_currency),
    'output_currency': check_currency(output_currency)}

    try:
        result = jsonify(**cuco.main(payload))
    except ValueError:
        return '<h2>Number Value Error</h2>\nProvided input for amount is not correct.'
    except KeyError:
        return '<h2>Key Error</h2>\nMissing required input values (amount, input_currency) or provided unsupported currency code.\n'
    else:
        return result


if __name__ == "__main__":
	app.run(debug=True)
