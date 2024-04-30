import pandas as pd
import argparse

import plotly.graph_objects as go

class Visualization:
    def __init__(self):
        pass

    def plot_stock_data(self, ticker, start_date, end_date):
        """
        Plots the candlestick chart for a given stock ticker and range of dates.

        Parameters:
        ticker (str): The stock ticker symbol.
        start_date (str): The start date of the range in YYYY-MM-DD format.
        end_date (str): The end date of the range in YYYY-MM-DD format.

        Returns:
        None
        """
        # Read the stock data from CSV file
        df = pd.read_csv(f'../data/symbols/{ticker}_5min_stock_data.csv')

        # Convert 'Timestamp' to DateTime if not already done
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])

        # Filter the DataFrame based on the range of dates
        filtered_df = df[(df['Timestamp'].dt.date >= pd.to_datetime(start_date).date()) &
                         (df['Timestamp'].dt.date <= pd.to_datetime(end_date).date())]

        # Create the candlestick chart
        fig = go.Figure(data=[go.Candlestick(x=filtered_df['Timestamp'],
                             open=filtered_df['Open'],
                             high=filtered_df['High'],
                             low=filtered_df['Low'],
                             close=filtered_df['Close'])])

        # Add title to the chart
        fig.update_layout(title=f'Candlestick Chart for {ticker} ({start_date} to {end_date})')

        # Show the plot
        fig.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ticker', help='The stock ticker symbol')
    parser.add_argument('--start_date', help='The start date of the range in YYYY-MM-DD format')
    parser.add_argument('--end_date', help='The end date of the range in YYYY-MM-DD format')
    args = parser.parse_args()

    visualization = Visualization()

    if args.ticker and args.start_date and args.end_date:
        visualization.plot_stock_data(args.ticker, args.start_date, args.end_date)
    else:
        ticker = input("Jim, which ticker is mickeying today?: ")
        start_date = input("Enter the start date in YYYY-MM-DD format: ")
        end_date = input("Enter the end date in YYYY-MM-DD format: ")
        visualization.plot_stock_data(ticker, start_date, end_date)





    
