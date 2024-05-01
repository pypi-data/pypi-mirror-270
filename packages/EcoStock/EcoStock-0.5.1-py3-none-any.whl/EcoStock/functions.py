# Nel file functions.py, includeremo tutte le funzioni per ottenere i dati finanziari e economici ecc...
# ESEMPIO:
# EcoStock/functions.py

import pandas as pd
import numpy as np
import requests
import yfinance as yf
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from plotly.subplots import make_subplots
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
import warnings

# Fetching stock data
def get_stock_data(ticker, start_date, end_date):
    """
    Fetch stock data from Yahoo Finance.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
    pandas.DataFrame: DataFrame containing the stock data.
    """
    return yf.download(ticker, start=start_date, end=end_date)

# Plotting the stock data
def plot_candlestick(ticker, start_date, end_date):
    """
    Fetch the stock data and plot it as a candlestick chart.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.
    """
    # Fetch the stock data
    stock_data = get_stock_data(ticker, start_date, end_date)

    # Create a candlestick chart
    fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                         open=stock_data['Open'],
                                         high=stock_data['High'],
                                         low=stock_data['Low'],
                                         close=stock_data['Close'])])

    # Add volume bars
    fig.add_trace(go.Bar(x=stock_data.index, y=stock_data['Volume'], marker=dict(color=np.where(stock_data['Close'] >= stock_data['Open'], 'green', 'red')), yaxis='y2'))

    # Add range slider
    fig.update_layout(
        title=f'{ticker} Stock Price',
        yaxis_title='Stock Price (USD)',
        shapes = [dict(x0='2022-01-01', x1='2022-12-31', y0=0, y1=1, xref='x', yref='paper', line_width=2)],
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(visible=True),
            type="date"
        ),
        yaxis2=dict(domain=[0, 0.2], anchor='x', title='Volume')
    )

    # Display the plot
    return fig.show()

# Calculate the 1-year moving average stock data
def moving_avg_stock_data(ticker, start_date, end_date):
    """
    Fetch stock data from Yahoo Finance and calculate a 1-year moving average, then resample to annual frequency.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    start_year (str): Start year in 'YYYY' format.
    end_year (str): End year in 'YYYY' format.

    Returns:
    pandas.DataFrame: DataFrame containing the 1-year moving average stock data, resampled to annual frequency.
    """
    # Format the years as 'YYYY-MM-DD'
    start_date = f'{start_date}-01-01'
    end_date = f'{end_date}-12-31'

    # Fetch the daily stock data
    df = yf.download(ticker, start=start_date, end=end_date)

    # Calculate a 1-year moving average
    df = df.rolling(window=252).mean()

    # Resample to annual frequency, taking the last observation of each year
    df = df.resample('Y').last()

    # Modify the index to only include the year
    df.index = df.index.year

    return df

# World Bank data
def get_world_bank_data(indicator, country, start_date, end_date):
    """
    Fetch economic data from the World Bank.

    Parameters:
    indicator (str): The indicator of interest.
    country (str): The country of interest.
    start_date (str): The start date for the data.
    end_date (str): The end date for the data.

    Returns:
    pandas.DataFrame: DataFrame containing the economic data.
    """
    if not indicator:
        print(f"Error: Unknown indicator input '{indicator}'")
        return pd.DataFrame()
    
    # Define the API URL
    url = f"http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?date={start_date}:{end_date}&format=json"

    # Send the HTTP request and get the response
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the data from the response
        data = response.json()

        # Check if the data has at least two elements
        if len(data) < 2:
            print("Error: No data available for the given parameters")
            return pd.DataFrame()

        # Convert the data to a DataFrame and set the date as the index
        df = pd.DataFrame(data[1])
        df['date'] = pd.to_datetime(df['date']).dt.year
        df.set_index('date', inplace=True)

        # Extract the name of the indicator and the country
        df['indicator'] = df['indicator'].apply(lambda x: x['value'])
        df['country'] = df['country'].apply(lambda x: x['value'])

        return df
    else:
        print(f"Error: HTTP request failed with status code {response.status_code}")
        return pd.DataFrame()

def plot_correlation(ticker, indicator, country, start_date, end_date):
    """
    Fetch stock data from Yahoo Finance and calculate a 1-year moving average, then fetch economic data from the World Bank, 
    and plot the correlation between stock and economic data over time.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    indicator (str): The indicator of interest for the World Bank data.
    country (str): The country of interest for the World Bank data.
    start_date (str): The start date for the data.
    end_date (str): The end date for the data.
    econ_label (str): Label for the economic data.
    econ_format (str): Format of the economic data ('dollar', 'percent', or None). Default is None.
    """
    # Fetch the 1-year moving average stock data
    stock_data = moving_avg_stock_data(ticker, start_date, end_date)

    # Fetch the economic data from the World Bank
    econ_data = get_world_bank_data(indicator, country, start_date, end_date)
    
    # Get the econ_label from the econ_data DataFrame
    econ_label = econ_data['indicator'].iloc[0]

    # Determine the econ_format based on the econ_label
    if '$' in econ_label:
        econ_format = 'US$'
    elif '%' in econ_label:
        econ_format = '%'
    else:
        econ_format = None

    # Merge the data
    merged_data = pd.merge(stock_data, econ_data, how='inner', left_index=True, right_index=True)

    # Check if merged_data is empty
    if merged_data.empty:
        print("Error: No matching data found for stock_data and econ_data")
        return None

    # Calculate the correlation
    correlation = merged_data['Close'].corr(merged_data['value'])

    # Create the plot
    sns.set(style="darkgrid")
    fig, ax1 = plt.subplots(figsize=(10, 6))  # Increase the size of the plot

    color = 'tab:red'
    ax1.set_xlabel('Date')
    ax1.set_ylabel(f'{ticker} Price', color=color)
    ax1.plot(stock_data.index, stock_data['Close'], color=color, label=f'{ticker} Price')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel(econ_label, color=color)
    ax2.plot(econ_data.index, econ_data['value'], color=color, label=econ_label)
    ax2.tick_params(axis='y', labelcolor=color)

    # Format the y-tick labels based on econ_format
    if econ_format == '%':
        formatter = mticker.FuncFormatter(lambda x, pos: '{:.1f}%'.format(x))
    elif econ_format == 'US$':
        def human_format(num):
            magnitude = 0
            while abs(num) >= 1000:
                magnitude += 1
                num /= 1000.0
            return '${:.1f}{}'.format(num, ['', 'K', 'M', 'B', 'T'][magnitude])

        formatter = mticker.FuncFormatter(lambda x, pos: human_format(x))
    else:
        formatter = None

    if formatter is not None:
        ax2.yaxis.set_major_formatter(formatter)

    fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)
    plt.title(f'Correlation between {ticker} Price and {econ_label}: {correlation:.2f}')
    fig.tight_layout()
    
    return plt.show()

# Plotting Bollinger Bands
def plot_bollinger_bands(ticker, start_date, end_date):

    # Fetch the stock data
    data = get_stock_data(ticker, start_date, end_date)

    # Define the window size and number of standard deviations for the Bollinger Bands
    window_size = 20
    num_of_std = 2

    # Calculate the rolling mean of the 'Close' prices over the specified window size
    rolling_mean = data['Close'].rolling(window=window_size).mean()

    # Calculate the rolling standard deviation of the 'Close' prices over the specified window size
    rolling_std = data['Close'].rolling(window=window_size).std()

    # Calculate the upper Bollinger Band as the rolling mean plus a number of standard deviations
    upper_band = rolling_mean + (rolling_std * num_of_std)

    # Calculate the lower Bollinger Band as the rolling mean minus a number of standard deviations
    lower_band = rolling_mean - (rolling_std * num_of_std)

    # Create a candlestick chart with the 'Open', 'High', 'Low', and 'Close' prices
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])

    # Add the upper Bollinger Band to the chart as a red line
    fig.add_trace(go.Scatter(x=data.index, y=upper_band, name="Upper Band", line=dict(color='red')))

    # Add the rolling mean to the chart as a blue line
    fig.add_trace(go.Scatter(x=data.index, y=rolling_mean, name="Rolling Mean", line=dict(color='blue')))

    # Add the lower Bollinger Band to the chart as a green line
    fig.add_trace(go.Scatter(x=data.index, y=lower_band, name="Lower Band", line=dict(color='green')))

    # Set the title of the chart to 'Bollinger Bands for {ticker}'
    fig.update_layout(title='Bollinger Bands for {}'.format(ticker))

    # Display the chart
    fig.show()

# Plotting indicator data for multiple countries
def plot_indicator_for_countries(indicator, countries, start_date, end_date):
    """
    Plot an economic indicator for several countries.

    Parameters:
    indicator (str): The indicator of interest.
    countries (list): The countries of interest.
    start_date (str): The start date for the data.
    end_date (str): The end date for the data.
    """
    fig = go.Figure()

    indicator_name = None

    for country in countries:
        df = get_world_bank_data(indicator, country, start_date, end_date)
        if not df.empty:
            fig.add_trace(go.Scatter(x=df.index, y=df['value'], mode='lines', name=country))
            # Get the indicator name from the first row of the DataFrame
            if indicator_name is None:
                indicator_name = df['indicator'].iloc[0]

    if indicator_name is not None:
        fig.update_layout(title=f'{indicator_name} from {start_date} to {end_date}', xaxis_title='Year', yaxis_title=indicator_name)
    else:
        fig.update_layout(title=f'{indicator} from {start_date} to {end_date}', xaxis_title='Year', yaxis_title=indicator)

    fig.show()

# Plotting the correlation between stocks
def analyze_stock_correlation(tickers, start_date, end_date):
    # Get the stock data
    stock_data = pd.DataFrame()
    for ticker in tickers:
        data = get_stock_data(ticker, start_date, end_date)
        stock_data[ticker] = data['Close']
    
    # Calculate daily returns in percentage
    returns = stock_data.pct_change() * 100
    
    # Create a figure
    fig = go.Figure()

    # Define a list of colors for the lines
    colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']

    # Add traces for each symbol
    for i, symbol in enumerate(tickers):
        fig.add_trace(go.Scatter(x=returns.index, y=returns[symbol], name=symbol,
                                 line=dict(width=1, color=colors[i % len(colors)]), opacity=0.7))

    # Set the title and axis labels
    fig.update_layout(title='Daily Returns of Stocks',
                      xaxis_title='Date',
                      yaxis_title='Daily Return (%)',
                      autosize=False,
                      width=1000,
                      height=500,
                      margin=dict(l=50, r=50, b=100, t=100, pad=4),
                      paper_bgcolor="white",
                      plot_bgcolor='white')

    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(visible=True),
            type="date"
        )
    )

    # Show the figure
    fig.show()

# Plotting the stock prediction
def plot_stock_prediction(ticker, start_date, end_date):
    # Suppress warnings
    warnings.filterwarnings('ignore')

    # Get the stock data
    stock_data = get_stock_data(ticker, start_date, end_date)
    
    # Calculate moving averages
    stock_data['MA10'] = stock_data['Close'].rolling(10).mean()
    stock_data['MA50'] = stock_data['Close'].rolling(50).mean()
    
    # Calculate Bollinger Bands
    stock_data['20 Day MA'] = stock_data['Close'].rolling(window=20).mean()
    stock_data['20 Day STD'] = stock_data['Close'].rolling(window=20).std()
    stock_data['Upper Band'] = stock_data['20 Day MA'] + (stock_data['20 Day STD'] * 2)
    stock_data['Lower Band'] = stock_data['20 Day MA'] - (stock_data['20 Day STD'] * 2)
    
    # Calculate RSI
    delta = stock_data['Close'].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    average_gain = up.rolling(window=14).mean()
    average_loss = abs(down.rolling(window=14).mean())
    rs = average_gain / average_loss
    stock_data['RSI'] = 100 - (100 / (1 + rs))
    
    # Calculate MACD
    stock_data['26 EMA'] = stock_data['Close'].ewm(span=26).mean()
    stock_data['12 EMA'] = stock_data['Close'].ewm(span=12).mean()
    stock_data['MACD'] = stock_data['12 EMA'] - stock_data['26 EMA']
    stock_data['Signal Line'] = stock_data['MACD'].ewm(span=9).mean()
    
    # Fit the ARIMA model
    arima_order = (5,1,0)  # Hardcoded ARIMA order
    model = ARIMA(stock_data['Close'], order=arima_order)
    model_fit = model.fit()
    
    # Make the prediction
    forecast_result = model_fit.forecast(steps=1)
    prediction = forecast_result.iloc[0]

    # Create a new DataFrame for the prediction
    prediction_data = pd.DataFrame({'Close': [prediction]}, index=[pd.to_datetime(end_date) + pd.DateOffset(days=1)])

    # Concatenate the historical and prediction data
    full_data = pd.concat([stock_data, prediction_data])

    # Create subplots
    fig = make_subplots(rows=3, cols=1)

    # Add traces

    fig.add_trace(go.Scatter(x=full_data.index, y=full_data['Close'], mode='lines', name='Close Price', line=dict(color='darkblue')), row=1, col=1)
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['MA10'], mode='lines', name='10-day MA', line=dict(color='darkred')), row=1, col=1)
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['MA50'], mode='lines', name='50-day MA', line=dict(color='darkgreen')), row=1, col=1)
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Upper Band'], mode='lines', name='Upper Bollinger Band', line=dict(color='indigo')), row=1, col=1)
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Lower Band'], mode='lines', name='Lower Bollinger Band', line=dict(color='darkorange')), row=1, col=1)
    fig.add_trace(go.Scatter(x=prediction_data.index, y=prediction_data['Close'], mode='markers', name='Predicted Price', marker=dict(color='red', size=10)), row=1, col=1)

    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['RSI'], mode='lines', name='RSI', line=dict(color='teal')), row=2, col=1)

    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['MACD'], mode='lines', name='MACD', line=dict(color='darkviolet')), row=3, col=1)
    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Signal Line'], mode='lines', name='Signal Line', line=dict(color='gold')), row=3, col=1)

    # Update xaxis properties
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_xaxes(title_text="Date", row=3, col=1)

    # Update yaxis properties
    fig.update_yaxes(title_text="Price", row=1, col=1)
    fig.update_yaxes(title_text="RSI", row=2, col=1)
    fig.update_yaxes(title_text="MACD", row=3, col=1)

    # Update title and size
    fig.update_layout(height=800, width=1000, title_text=f"{ticker} Stock Price Prediction: {prediction:.2f}$")

    fig.show()

# Plotting the portfolio return
def plot_portfolio_return(tickers, start_date, end_date):
    """
    Calculate the overall return of a portfolio.

    Parameters:
    tickers (list): A list of ticker symbols.
    start_date (str): The start date in format 'yyyy-mm-dd'.
    end_date (str): The end date in format 'yyyy-mm-dd'.

    Returns:
    DataFrame: The cumulative returns of the portfolio over time.
    """
    # Initialize the portfolio return as an empty DataFrame
    portfolio_return = pd.DataFrame()

    # For each ticker symbol
    for ticker in tickers:
        # Get the stock data
        stock_data = get_stock_data(ticker, start_date, end_date)

        # Calculate the daily return
        stock_data['Return'] = stock_data['Close'].pct_change()

        # If the portfolio return DataFrame is empty, copy the return data from the current stock
        if portfolio_return.empty:
            portfolio_return = stock_data[['Return']].copy()
            portfolio_return.columns = [ticker]
        else:
            # Otherwise, join the return data from the current stock
            portfolio_return = portfolio_return.join(stock_data['Return'], how='outer', rsuffix=ticker)

    # Calculate the average daily return
    portfolio_return['Average'] = portfolio_return.mean(axis=1)

    # Calculate the cumulative return
    portfolio_return['Cumulative'] = (1 + portfolio_return['Average']).cumprod()

    # Convert the cumulative return to percentage
    portfolio_return['Cumulative'] = portfolio_return['Cumulative'] * 100

    # Create a plotly graph object for the cumulative return
    fig = go.Figure(data=go.Scatter(x=portfolio_return.index, y=portfolio_return['Cumulative']))

    # Add title and labels
    fig.update_layout(title='Portfolio Cumulative Returns', xaxis_title='Date', yaxis_title='Cumulative Return (%)')

    # Show the plot
    fig.show()

