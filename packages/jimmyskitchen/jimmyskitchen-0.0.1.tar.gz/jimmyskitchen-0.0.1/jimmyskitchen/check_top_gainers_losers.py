import requests
import pandas as pd
import os
import datetime
import sys

# Get API key from environment variable
api_key = os.getenv('API_KEY')

# API KEY
class DataScrapper:
    def get_topgainers(self, api_key=None):
        if api_key is None:
            api_key = os.getenv('API_KEY')

        url = f'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={api_key}'

        r = requests.get(url)
        data = r.json()

        top_gainers = data['top_gainers']
        df_topgainers = pd.DataFrame(top_gainers)
        now = datetime.datetime.now()

        # Format the date and time as a string
        date_string = now.strftime("%Y-%m-%d")
        # Save the DataFrame as a CSV file
        df_topgainers.to_csv(f'../data/gainers/top_gainers_{date_string}.csv', index=False)
        print(f'Data has been written to {df_topgainers}')

    def get_toplosers(self, api_key=None):
        if api_key is None:
            api_key = os.getenv('API_KEY')

        url = f'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={api_key}'

        r = requests.get(url)
        data = r.json()

        top_losers = data['top_losers']
        df_toplosers = pd.DataFrame(top_losers)

        now = datetime.datetime.now()

        # Format the date and time as a string
        date_string = now.strftime("%Y-%m-%d")
        # Save the DataFrame as a CSV file
        df_toplosers.to_csv(f'../data/losers/top_losers_{date_string}.csv', index=False)
        print(f'Data has been written to {df_toplosers}')

if __name__ == "__main__":
    data_scrapper = DataScrapper()

    # Check if arguments are provided
    if len(sys.argv) > 1:
        if sys.argv[1] == 'topgainers':
            data_scrapper.get_topgainers()
        elif sys.argv[1] == 'toplosers':
            data_scrapper.get_toplosers()
        else:
            print('Invalid argument. Please provide either "topgainers" or "toplosers".')
    else:
        data_scrapper.get_topgainers()
        data_scrapper.get_toplosers()