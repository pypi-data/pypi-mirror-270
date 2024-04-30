import argparse
import pandas as pd

import plotly.graph_objects as go

class StockAnalyzer:
    def __init__(self, ticker):
        self.ticker = ticker

    def analyze_volume_extended(self, desired_date):
        file_path = f'../data/symbols/{self.ticker}_5min_stock_data.csv'
        df = pd.read_csv(file_path)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])  # Convert Timestamp column to datetime type

        # Filter the DataFrame based on the desired date
        filtered_df = df[df['Timestamp'].dt.date == desired_date]

        # Calculate the differences in volume for the filtered DataFrame
        filtered_df['Volume'] = filtered_df['Volume'].diff()

        figreturns = go.Scatter(x=filtered_df['Timestamp'], y=filtered_df['Volume'], mode='lines', name='Volume')

        fig = go.Figure([figreturns])
        fig.update_layout(title=f'{self.ticker} Volume',
                          xaxis_title='Timestamp',
                          yaxis_title='Volume',
                          yaxis=dict(range=[filtered_df['Volume'].min() - 0.01, filtered_df['Volume'].max() + 0.01]),
                          margin=dict(l=50, r=50, t=50, b=50))

        fig.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ticker', help='Ticker symbol')
    parser.add_argument('--date', help='Desired date (YYYY-MM-DD)')
    args = parser.parse_args()

    if args.ticker and args.date:
        analyzer = StockAnalyzer(args.ticker)
        analyzer.analyze_volume_extended(pd.to_datetime(args.date).date())
    else:
        ticker = input("Enter the ticker symbol: ")
        desired_date = pd.to_datetime(input("Enter the desired date (YYYY-MM-DD): ")).date()
        analyzer = StockAnalyzer(ticker)
        analyzer.analyze_volume_extended(desired_date)
