# Import required modules
import requests
from datetime import datetime 

# Function to fetch historical exchange rates from the Frankfurter API
def historical_exchange_rate(amount, from_currency, to_currency, date):
    print("\nFetching exchange rates...")
    # Construct the API URL with required parameters
    base_url = f"https://api.frankfurter.app/{date}?amount={amount}&from={from_currency}&to={to_currency}"

    # Send a GET request to the API
    response = requests.get(base_url)

    # Check if the request was successful
    if response.status_code == 200:
        # If successful, convert the response to JSON
        data = response.json()
        # Return the exchange rate
        return data['rates'][f'{to_currency}']
    else:
        # If unsuccessful, return an error message
        return "Error in the API request."

# Function to handle date input from the user
def input_date():
    while True:
        # Ask the user to input a date
        date_str = input("Please enter a date (e.g. 2022-12-01): ")
        try:
            # Try to parse the input to a datetime object
            date = datetime.strptime(date_str, '%Y-%m-%d')
            # Check if the date is valid (i.e., not in the future and in the correct format)
            if date_str != datetime.strftime(date, '%Y-%m-%d') or date > datetime.now():
                raise ValueError()
            # If valid, return the date
            return date_str
        except ValueError:
            # If invalid, inform the user and loop again
            print("\nInvalid date. Please enter a past or present date in the following format: YYYY-MM-DD (e.g. 2022-12-01).")

# Function to handle currency input from the user
def input_currency(prompt):
    while True:
        # Ask the user to input a currency
        currency = input(prompt).upper()
        # Check if the input is valid (i.e., a three-letter string)
        if len(currency) == 3 and currency.isalpha():
            # If valid, return the currency
            return currency
        else:
            # If invalid, inform the user and loop again
            print("\nInvalid currency. Please use the 3-letter currency code (e.g. USD).")

# Function to handle amount input from the user
def input_amount():
    while True:
        try:
            # Ask the user to input an amount and try to convert it to a float
            return float(input("Enter the amount to be converted: "))
        except ValueError:
            # If the input cannot be converted to a float, inform the user and loop again
            print("Invalid amount. Please enter a number.")

# Main program loop
while True:
    # Print a welcome message and instructions
    print("\n==Welcome to the Historical Currency Converter!==\n")
    print("Instructions:\nEnter the currencies in their 3-letter code (e.g. USD).\nEnter the amount as a whole or decimal number (e.g. 12.34).\nEnter the date in the ISO 8601 format (e.g. 2022-12-01).\n")

    # Collect inputs from the user
    print("User input:")
    from_currency = input_currency("Enter the currency you want to convert from (e.g. USD): ")
    to_currency = input_currency("Enter the currency you want to convert to: ")
    amount = input_amount()
    date = input_date()

    # Confirm the inputs with the user
    print(f"\nYou want to convert {amount} {from_currency} to {to_currency} on {date}. Is that correct? (Y/N): ")
    confirmation = input().lower()

    # If the user confirms, fetch the exchange rate and print the result
    if confirmation in ['y', 'yes']:
        result = historical_exchange_rate(amount, from_currency, to_currency, date)

        if isinstance(result, float):
            print(f"\n{amount} {from_currency} was equivalent to {result} {to_currency} on {date}.\n")
        else:
            print(result)
        break
    # If the user denies, start over
    elif confirmation in ['n', 'no']:
        print("\nAlright, let's start over.")
    else:
        # If the input is not 'yes' or 'no', inform the user and ask again
        print("\nInvalid input, please enter 'Y' for yes or 'N' for no.")