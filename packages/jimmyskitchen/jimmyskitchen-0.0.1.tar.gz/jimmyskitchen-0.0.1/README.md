# Jim's Kitchen
Jim's Kitchen is a framework helping you understand the US-Stock Market. It focuses on returns and correlation analysis but also has an sentiment analysis extension. The public version has a few functions that are only for visualization and understanding the processes of the models.

<table>
  <tr>
    <td>
      <img src="https://wandb.ai/logo.png" alt="Wandb" width="300" height="300">
    </td>
    <td>
      <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Plotly-logo.png" alt="Image 2" width="600" height="200">
    </td>
  </tr>
</table>


<table>
  <tr>
    <td>
      <img src="https://miro.medium.com/v2/resize:fit:1034/1*JupRAYk4Q2xyEBWVV4SNyg.jpeg" alt="Wandb" width="300" height="200">
    </td>
    <td>
      <img src="https://www.datanami.com/wp-content/uploads/2023/06/kx-python.png" alt="Image 2" width="600" height="200">
    </td>
  </tr>
</table>

**Note: The Python implementation is just for demonstration and visualization purposes. The real streaming and processing of the date will be done through [kdb+/q](https://code.kx.com/q/).**

## Returns Analysis:

In the returns analysis only three stock exchanges are considered. These are the New York Stock Exchange (NYSE), Nasdaq Stock Market (NASDAQ) and the Chicago Stock Exchange (CBOE). The framework covers over 5000+ stocks. The goal is to track them simultaneously and compute the returns of the Price at time t (which is the current API CALL) and the last Price at the time t-1 (last API CALL before the current one).

General case:

$Returns_{ij} = \frac{P_{i, t}}{P_{i, t-k}} - 1$
$\quad i = 1, \dots, n$

where $n$ is the number of tracked stocks, $P$ can be the current/open/high/low or close price of the stock, 
and $t$ is the time. $k$ is the number of API calls before the current one.

The returns are computed for multiple events. The first one is the simple case which is you take the current price of your API Call and divide it with the last API Call, to normalize it you substract 1.
Other cases are basically aggregations of the simple case to reduce some noise in the data. We make the assumption that the API server is called every second, t is secondwise. This brings use to the next return computations.

1s:

$Returns_{ij} = \frac{P_{i, t}}{P_{i, t-1}} - 1$
$\quad i = 1, \dots, n$

5s:

$Returns_{ij} = \frac{P_{i, t}}{P_{i, t-5}} - 1$
$\quad i = 1, \dots, n$

10s:

$Returns_{ij} = \frac{P_{i, t}}{P_{i, t-10}} - 1$
$\quad i = 1, \dots, n$

30s:

$Returns_{ij} = \frac{P_{i, t}}{P_{i, t-30}} - 1$
$\quad i = 1, \dots, n$

1min:

$Returns_{ij} = \frac{P_{i, t}}{P_{i, t-60}} - 1$
$\quad i = 1, \dots, n$

5min:

$Returns_{ij} = \frac{P_{i, t}}{P_{i, t-300}} - 1$
$\quad i = 1, \dots, n$

10min:

$Returns_{ij} = \frac{P_{i, t}}{P_{i, t-600}} - 1$
$\quad i = 1, \dots, n$

So we basically keep track of the stock returns in different timeframes for all 5000+ stocks. This means we need a big data warehouse that can process this amount of data. This is a challenging problem therefore in this academic setting I will only keep track of the one hundred most traded stocks. 

After setting up the data infrastructure to compute and store the returns, the next step is to make it in a format suitable for a NLP model. Also expertise knowledge is needed for choosing a suitable NLP model. (!!! One of my Bachelor Thesis Goals)

To see which model performs the best, we will have to train and test multiple ones. The testing will be done via Weights and Biases AI (wandb AI), which is a framework for monitoring your model.

### Visualization of the returns function for OHLC Prices
The default is the OHLC Prices plot but you can choose which of the OHLC you want to turn on/off.

**OHLC Prices**
```python
from check_returns_extented import StockAnalyzer

stock_analyse = StockAnalyzer()

stock_analyse.analyze_returns_extended('NVDA', '2024-04-23')
```
![Fullreturnfunction](https://github.com/JuliusLhamo/JimsKitchenPublic/blob/main/pngs/returnsfull.png?raw=true)

![OCreturnfunction](https://github.com/JuliusLhamo/JimsKitchenPublic/blob/main/pngs/returns.png?raw=true)

This is the return function of NVDA on the day 2024-04-23.

## Stock Correlation analysis:
We compute the pearson correlation for all 5000+ stocks. So we have a n x n correlation matrix with n being the number of stocks.

$r = \frac{{\sum (X_i - \bar{X})(Y_i - \bar{Y})}}{{\sqrt{\sum (X_i - \bar{X})^2 \sum (Y_i - \bar{Y})^2}}}$

Where:
- $X_i$ and $Y_i$ are individual data points (prices) of stocks X and Y respectively,
- $\bar{X}$ and $\bar{Y}$ are the means of variables X and Y respectively,
- $\sum$ represents the sum over all data points, and
- $r$ is the Pearson correlation coefficient.

For demonstration purposes, I visualized a small scale of the correlation matrix.
![ok](https://github.com/JuliusLhamo/JimsKitchenPublic/blob/main/pngs/example_correlation_mat.png?raw=true)

Now we do the same steps as in the returns analysis where we compute the pearson correlation for different timeframes


## Volume analysis

```python
from check_volume_change import StockAnalyser

stock_analyser = StockAnalyser()

stock_analyser.analyze_volume_extended(ticker = 'NVDA', desired_date = '2024-04-23')
```
Visualization Example of NVDA 2024-04-23
![NVDA_Volume](https://github.com/JuliusLhamo/JimsKitchenPublic/blob/main/pngs/example_volume_analysis.png?raw=true)

## Helper Functions
This framework contains a list of helper functions assisting the user when testing/using the model.

### Visualization of the chart
With this function the user can choose the ticker, the start date and end date of the stock

```python
from check_chart_extended import Visualization

vis = Visualization()

vis.plot_stock_data(ticker = 'CDLX', start_date = '2024-03-28', end_date = '2024-03-28')
```
![Chart_example](https://github.com/JuliusLhamo/JimsKitchenPublic/blob/main/pngs/chart_cdlx.png?raw=true)


### Importing of the ticker data
We use Alpha Vintage API as Rest API server. The function takes the argument 'ticker' which can be a list or a single str.
The imported data is saved in a csv file.

```python
from import_data import DataImport 

data_import = DataImport()

#For example
data_import.download_stock_data(ticker = 'IBRX')

```
Example for Data Import output:
![Csv_file](https://github.com/JuliusLhamo/JimsKitchenPublic/blob/main/pngs/example_csv_df.png?raw=true)
### Identifying the Gainers and Losers of the day
This function identifies all gainers and losers of the day.

#### Top Stocks Gainer List
```python
from check_top_gainers_losers.py import DataScrapper

data_scrapper = DataScrapper()

#For example for a list of top gainers
data_scrapper.get_topgainers()
```
![Top_gainers](https://github.com/JuliusLhamo/JimsKitchenPublic/blob/main/pngs/example_for_top_gainers.png?raw=true)


#### Top Stocks Loser List

```python
from check_top_gainers_losers.py import DataScrapper

data_scrapper = DataScrapper()

#For example for a list of top losers
data_scrapper.get_toplosers()
```
![Top_Losers](https://github.com/JuliusLhamo/JimsKitchenPublic/blob/main/pngs/example_for_top_losers.png?raw=true)
