import pandas as pd
from import_data import DataImport

def download_stock_data_by_date(date):
    data_gainers = pd.read_csv(f'../data/gainers/top_gainers_{date}.csv')
    print(data_gainers)
    list_gainers = data_gainers['ticker'].tolist()
    print(list_gainers)
    data_import = DataImport()

    for ticker in list_gainers:
        try:
            data_import.download_stock_data(ticker)
        except Exception as e:
            print(f"Failed to download data for ticker {ticker}. Skipping...")
            continue


if __name__ == "__main__":
    date = input("Enter the date: ")
    download_stock_data_by_date(date)
