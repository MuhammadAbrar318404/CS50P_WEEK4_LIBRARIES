import sys  # Import the sys module to access command-line arguments
import requests  # Import the requests module to make HTTP requests

def main():
    if len(sys.argv) != 2:  # Check if the number of command-line arguments is not equal to 2
        print("Missing command-line argument")  # Print an error message if argument is missing
        sys.exit(1)  # Exit the program with status code 1

    try:
        bitcoin_amount = float(sys.argv[1])  # Try to convert the argument to a float
    except ValueError:  # Handle the exception if the argument is not a valid number
        print("Command-line argument is not a number")  # Print an error message if the argument is not a number
        sys.exit(1)  # Exit the program with status code 1

    cost = calculate_cost(bitcoin_amount)  # Calculate the cost based on the Bitcoin amount
    print(f"${cost:,.4f}")  # Print the cost formatted to 4 decimal places

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')  # Fetch the current Bitcoin price
        data = response.json()  # Parse the response as JSON
        return float(data['bpi']['USD']['rate'].replace(',', ''))  # Extract and return the Bitcoin price in USD
    except (requests.RequestException, KeyError, ValueError):  # Handle possible exceptions during the request and parsing
        print("Error fetching Bitcoin price.")  # Print an error message if there's an issue fetching the price
        sys.exit(1)  # Exit the program with status code 1

def calculate_cost(bitcoin_amount):
    bitcoin_price = get_bitcoin_price()  # Get the current Bitcoin price
    cost = bitcoin_amount * bitcoin_price  # Calculate the cost based on the Bitcoin amount and price
    return cost  # Return the calculated cost

main()  # Call the main function to start the program
