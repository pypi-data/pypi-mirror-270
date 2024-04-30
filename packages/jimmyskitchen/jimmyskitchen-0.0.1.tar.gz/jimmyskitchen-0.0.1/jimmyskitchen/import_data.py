import argparse
import requests
import csv
from tabulate import tabulate
from dotenv import load_dotenv
import os

class DataImport:
    def __init__(self):
        # Get the API key from the environment variable
        self.api_key = os.getenv('API_KEY')

    def download_stock_data(self, ticker):
        # Create the URL
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&outputsize=full&interval=5min&datatype=json&apikey={self.api_key}'

        # Send a request to the URL
        r = requests.get(url)

        # Convert the response to JSON
        data = r.json()

        # Extract the time series data
        time_series_data = data['Time Series (5min)']

        # Create a list to hold the data
        data_list = []

        # Iterate over the time series data
        for key, value in time_series_data.items():
            # Create a list for each row
            row = [key, value['1. open'], value['2. high'], value['3. low'], value['4. close'], value['5. volume']]
            # Add the row to the data list
            data_list.append(row)

        # Create a file name
        file_name = f'../data/symbols/{ticker}_5min_stock_data.csv'

        # Write the data to a csv file
        with open(file_name, 'w', newline='') as csvfile:
            # Create a csv writer
            writer = csv.writer(csvfile)
            # Write the header row
            writer.writerow(['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
            # Write the data rows
            writer.writerows(data_list)

        print(f'Data has been written to {file_name}')

if __name__ == '__main__':
    load_dotenv()  # Load environment variables from .env file

    # Create an argument parser
    parser = argparse.ArgumentParser(description='Download stock data.')

    # Add an argument for the ticker
    parser.add_argument('ticker', nargs='?', help='Ticker symbol')

    # Parse the arguments
    args = parser.parse_args()

    data_import = DataImport()

    if args.ticker:
        # If a ticker is provided as an argument, call the function with the ticker
        data_import.download_stock_data(args.ticker)
    else:
        # If no ticker is provided as an argument, prompt the user to enter the tickers
        tickers = input("Enter the tickers (separated by commas): ").split(',')
        for ticker in tickers:
            data_import.download_stock_data(ticker.strip())
