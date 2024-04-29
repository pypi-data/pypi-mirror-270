# Nel file functions.py, includeremo tutte le funzioni per ottenere i dati finanziari e economici ecc...
# ESEMPIO:
# EcoStock/functions.py

import pandas as pd
import numpy as np
import requests
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

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

    return fig

# Calculate the 1-year moving average stock data
def moving_avg_stock_data(ticker, start_year, end_year):
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
    start_date = f'{start_year}-01-01'
    end_date = f'{end_year}-12-31'

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

def plot_correlation(ticker, start_year, end_year, indicator, country, start_date, end_date, econ_label, econ_format=None):
    """
    Fetch stock data from Yahoo Finance and calculate a 1-year moving average, then fetch economic data from the World Bank, 
    and plot the correlation between stock and economic data over time.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    start_year (str): Start year for the stock data in 'YYYY' format.
    end_year (str): End year for the stock data in 'YYYY' format.
    indicator (str): The indicator of interest for the World Bank data.
    country (str): The country of interest for the World Bank data.
    start_date (str): The start date for the World Bank data.
    end_date (str): The end date for the World Bank data.
    econ_label (str): Label for the economic data.
    econ_format (str): Format of the economic data ('dollar', 'percent', or None). Default is None.
    """
    # Fetch the 1-year moving average stock data
    stock_data = moving_avg_stock_data(ticker, start_year, end_year)

    # Fetch the economic data from the World Bank
    econ_data = get_world_bank_data(indicator, country, start_date, end_date)

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
    ax1.set_ylabel('Stock Price', color=color)
    ax1.plot(stock_data.index, stock_data['Close'], color=color, label='Stock Price')
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
    plt.title(f'Correlation between Stock Price and {econ_label}: {correlation:.2f}')
    fig.tight_layout()
    
    return fig

# Plotting Bollinger Bands
def plot_bollinger_bands(ticker, start_date, end_date, window_size, num_of_std):
    # Fetch the stock data
    data = get_stock_data(ticker, start_date, end_date)

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


# Compare economic indicators for different countries
def compare_indicators_countries(indicators, countries, start_date, end_date):
    """
    Compare economic indicators for different countries over a specified time period.

    Parameters:
    indicators (list of str): The indicators of interest.
    countries (list of str): The countries of interest.
    start_date (str): The start date for the data.
    end_date (str): The end date for the data.
    """
    # Initialize an empty DataFrame to store the data
    data = pd.DataFrame()

    # Fetch the data for each indicator and country
    for indicator in indicators:
        for country in countries:
            df = get_world_bank_data(indicator, country, start_date, end_date)
            data = pd.concat([data, df])

    # Check if the DataFrame is not empty
    if not data.empty:
        # Create an interactive line plot with Plotly
        fig = px.line(data, y='value', color='country', line_group='indicator', line_dash='indicator',
                      title='Cross-countries comparison of economic indicators',)

        # Show plot
        fig.show()
    else:
        print("No data to plot.")





