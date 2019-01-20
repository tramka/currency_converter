from flask import Flask, request, jsonify, render_template
import currency_converter as cuco
from currency_converter import check_currency, positive_value
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.route("/")
def home():
    """
    Returns main page with example of usage.

    Returns
    -------
    str
        Description of application.
    """

    return render_template("home.html")


@app.route("/about/")
def about():
    """
    Returns brief information about application.

    Returns
    -------
    str
        Description of application.
    """

    return render_template("about.html")


@app.route("/currency_converter", methods=["GET"])
def currency_converter():
    """
	Orchestrates conversion from one currency to other.

    Returns
    -------
	str
        Converted values.
    """

    amount = request.args.get("amount")
    input_currency = request.args.get("input_currency")
    output_currency = request.args.get("output_currency")

    try:
        payload = {
            "amount": positive_value(amount),
            "input_currency": check_currency(input_currency),
            "output_currency": check_currency(output_currency),
        }
    except Exception as e:
        return "<h2>Number Value Error</h2><p>{}</p>".format(e)

    try:
        result = jsonify(**cuco.main(payload))
        return result
    except KeyError:
        return render_template("400.html")


@app.errorhandler(400)
def key_error(e):
    """
    Handling bad request error.
    """
    return render_template("400.html")


@app.errorhandler(404)
def page_not_found(e):
    """
    Handling page not found error.
    """
    return render_template("404.html")


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handling internal server error.
    """
    return render_template("generic.html")


@app.errorhandler(Exception)
def unhandled_exception(e):
    """
    Handling other uncaught errors.
    """
    return render_template("generic.html")


if __name__ == "__main__":
    app.run(debug=False)
