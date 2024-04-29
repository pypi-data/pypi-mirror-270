import pandas as pd
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from EcoStock.functions import (get_stock_data, moving_avg_stock_data, get_world_bank_data)

def candlestick(ticker, start_date, end_date):
    """
    Fetch the stock data and plot it as a simple line chart.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.
    """
    try:
        # Fetch the stock data
        stock_data = get_stock_data(ticker, start_date, end_date)

        # Check if data is empty
        if stock_data.empty:
            print(f"No data available for {ticker} from {start_date} to {end_date}")
            return None

        # Create a simple line chart for closing prices
        fig, ax = plt.subplots(figsize=(10,6))
        ax.plot(stock_data.index, stock_data['Close'], label='Close Price')

        # Format date axis
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

        # Set title and labels
        ax.set_title(f'{ticker} Stock Price')
        ax.set_xlabel('Date')
        ax.set_ylabel('Stock Price (USD)')

        # Add grid and legend
        ax.grid(True)
        ax.legend()

        # Return the plot
        return fig

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def bollinger_bands(ticker, start_date, end_date, window_size, num_of_std):
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

    # Create a simple line chart
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(data.index, data['Close'], label='Close Price')
    ax.plot(data.index, upper_band, label='Upper Band', color='red')
    ax.plot(data.index, rolling_mean, label='Rolling Mean', color='blue')
    ax.plot(data.index, lower_band, label='Lower Band', color='green')

    # Set the title and labels
    ax.set_title('Bollinger Bands for {}'.format(ticker))
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')

    # Add a legend
    ax.legend()

    # Return the figure
    return fig

def indicator_for_countries(indicator, countries, start_date, end_date):
    """
    Plot an economic indicator for several countries.

    Parameters:
    indicator (str): The indicator of interest.
    countries (list): The countries of interest.
    start_date (str): The start date for the data.
    end_date (str): The end date for the data.

    Returns:
    fig: A matplotlib Figure object.
    """
    fig, ax = plt.subplots(figsize=(10,6))

    indicator_name = None

    for country in countries:
        df = get_world_bank_data(indicator, country, start_date, end_date)
        if not df.empty:
            ax.plot(df.index, df['value'], label=country)
            # Get the indicator name from the first row of the DataFrame
            if indicator_name is None:
                indicator_name = df['indicator'].iloc[0]

    if indicator_name is not None:
        ax.set_title(f'{indicator_name} from {start_date} to {end_date}')
        ax.set_ylabel(indicator_name)
    else:
        ax.set_title(f'{indicator} from {start_date} to {end_date}')
        ax.set_ylabel(indicator)

    ax.set_xlabel('Year')
    ax.legend()

    return fig

# Get news data from GNews API
def get_news(symbol):
    # GNews API
    api_key = '3dcc9727bfb88289097e7dee864baae4'

    # URL of GNews's search function
    url = f'https://gnews.io/api/v4/search?q={symbol}&token={api_key}'

    try:
        # Send a GET request to the API
        response = requests.get(url)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None

    # Parse the JSON response
    try:
        data = response.json()
    except ValueError:
        print('Error parsing JSON response')
        return None

    return data

def comparison_indicators_countries(indicators, countries, start_date, end_date):
    """
    Compare economic indicators for different countries over a specified time period.

    Parameters:
    indicators (list of str): The indicators of interest.
    countries (list of str): The countries of interest.
    start_date (str): The start date for the data.
    end_date (str): The end date for the data.

    Returns:
    fig: A matplotlib Figure object.
    """
    # Initialize an empty DataFrame to store the data
    data = pd.DataFrame()

    # Fetch the data for each indicator and country
    for indicator in indicators:
        for country in countries:
            df = get_world_bank_data(indicator, country, start_date, end_date)
            data = pd.concat([data, df])

    fig = None

    # Check if the DataFrame is not empty
    if not data.empty:
        fig, ax = plt.subplots(figsize=(10,6))
        for indicator in indicators:
            for country in countries:
                subset = data[(data['indicator'] == indicator) & (data['country'] == country)]
                if not subset.empty:
                    ax.plot(subset.index, subset['value'], label=f'{country} - {indicator}')

        ax.set_title('Cross-countries comparison of economic indicators')
        ax.set_xlabel('Year')
        ax.set_ylabel('Value')
        ax.legend()

    return fig