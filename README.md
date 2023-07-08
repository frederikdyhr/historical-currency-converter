# historical_currency_converter
A simple Python-based tool to convert currencies using historical exchange rates

Historical Currency Converter in Python
---------------------------------------

This repository contains a Python implementation of a historical currency converter. It is a command-line based tool where a user inputs an amount, source currency, target currency, and a past date to receive the equivalent value in the target currency on that date.

Functionality
-------------

The converter uses the Frankfurter API to fetch historical exchange rates:

1. The user is asked to input a date (in YYYY-MM-DD format), the currency they want to convert from (3-letter currency code), the currency they want to convert to (3-letter currency code), and the amount to be converted.
2. The program calls the Frankfurter API to get the historical exchange rate for the specified date and converts the input amount from the source currency to the target currency.
3. The equivalent amount in the target currency on the specified date is displayed.

Running the Program
---------------------

To run the converter, you will need Python 3 and the requests module. Use the following command in the terminal to start the tool:

python currency_converter.py

Installation
------------

Before running the script, ensure you have the necessary Python package requests installed. If not, you can install it using pip:

pip install requests
