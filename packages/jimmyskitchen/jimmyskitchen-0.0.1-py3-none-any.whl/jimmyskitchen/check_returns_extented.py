import pandas as pd

import plotly.graph_objects as go

class StockAnalyzer:
    def __init__(self):
        pass
    def analyze_returns_extended(self, ticker, desired_date):
        df = pd.read_csv(f'../data/symbols/{ticker}_5min_stock_data.csv')
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])  # Convert Timestamp column to datetime type

        # Filter the DataFrame based on the desired date
        filtered_df = df[df['Timestamp'].dt.date == pd.to_datetime(desired_date).date()]

        # Calculate the returns for the filtered DataFrame
        filtered_df.loc[:, 'Returns_Open'] = filtered_df['Open'].pct_change()
        filtered_df.loc[:, 'Returns_High'] = filtered_df['High'].pct_change()
        filtered_df.loc[:, 'Returns_Low'] = filtered_df['Low'].pct_change()
        filtered_df.loc[:, 'Returns_Close'] = filtered_df['Close'].pct_change()

        figreturns = go.Scatter(x=filtered_df['Timestamp'], y=filtered_df['Returns_Close'], mode='lines', name='Returns_Close')
        figreturns_high = go.Scatter(x=filtered_df['Timestamp'], y=filtered_df['Returns_High'], mode='lines', name='Returns_High')
        figreturns_low = go.Scatter(x=filtered_df['Timestamp'], y=filtered_df['Returns_Low'], mode='lines', name='Returns_Low')
        figreturns_open = go.Scatter(x=filtered_df['Timestamp'], y=filtered_df['Returns_Open'], mode='lines', name='Returns_Open')

        fig = go.Figure([figreturns, figreturns_high, figreturns_low, figreturns_open])
        fig.update_layout(title=f'{ticker} Returns',
                          xaxis_title='Timestamp',
                          yaxis_title='Returns',
                          yaxis=dict(range=[filtered_df['Returns_Close'].min() - 0.01, filtered_df['Returns_Close'].max() + 0.01]),
                          margin=dict(l=50, r=50, t=50, b=50))

        fig.show()

if __name__ == '__main__':
    ticker = input("Enter the ticker symbol: ")
    desired_date = input("Enter the desired date (YYYY-MM-DD): ")
    analyzer = StockAnalyzer()
    analyzer.analyze_returns_extended(ticker, desired_date)
    def main():
        ticker = input("Enter the ticker symbol: ")
        desired_date = input("Enter the desired date (YYYY-MM-DD): ")
        analyzer = StockAnalyzer()
        analyzer.analyze_returns_extended(ticker, desired_date)

    if __name__ == '__main__':
        main()