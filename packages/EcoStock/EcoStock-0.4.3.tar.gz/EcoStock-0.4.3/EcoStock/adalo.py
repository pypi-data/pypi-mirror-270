import pandas as pd
import requests
import io
from io import BytesIO
import base64
import itertools
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import matplotlib.ticker as mticker
from EcoStock.functions import (get_stock_data, moving_avg_stock_data, get_world_bank_data)

def candlestick(ticker, start_date, end_date):
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
        locator = mdates.AutoDateLocator()
        formatter = mdates.AutoDateFormatter(locator)
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)

        # Set title and labels
        ax.set_title(f'{ticker} Stock Price')
        ax.set_xlabel('Date')
        ax.set_ylabel('Stock Price (USD)')

        # Add grid and legend
        ax.grid(True)
        ax.legend()

        # Auto format date labels
        fig.autofmt_xdate()

        # Save the plot to a BytesIO object
        buf = BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)

        # Convert the buffer contents to base64 and return
        return base64.b64encode(buf.getbuffer()).decode("ascii")

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def correlation(ticker, start_year, end_year, indicator, country, start_date, end_date, econ_label, econ_format=None):
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
        # Save the plot to a BytesIO object
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)

    # Convert the buffer contents to base64 and return
    return base64.b64encode(buf.getbuffer()).decode("ascii")

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

    # Format date axis
    locator = mdates.AutoDateLocator()
    formatter = mdates.AutoDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    # Auto format date labels
    fig.autofmt_xdate()

    # Save the plot to a BytesIO object
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)

    # Convert the buffer contents to base64 and return
    return base64.b64encode(buf.getbuffer()).decode("ascii")

def indicator_for_countries(indicator, countries, start_date, end_date, econ_format=None):
    """
    Plot an economic indicator for several countries.

    Parameters:
    indicator (str): The indicator of interest.
    countries (list): The countries of interest.
    start_date (str): The start date for the data.
    end_date (str): The end date for the data.
    econ_format (str): Format of the economic data ('dollar', 'percent', or None). Default is None.
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
        ax.yaxis.set_major_formatter(formatter)

    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)

    # Convert the buffer contents to base64 and return
    return base64.b64encode(buf.getbuffer()).decode("ascii")

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

def comparison_indicators_countries(indicators, countries, start_date, end_date, econ_format=None):
    """
    Plot multiple economic indicators for several countries in a single plot.

    Parameters:
    indicators (list): The indicators of interest.
    countries (list): The countries of interest.
    start_date (str): The start date for the data.
    end_date (str): The end date for the data.
    econ_format (str): Format of the economic data ('dollar', 'percent', or None). Default is None.
    """
    fig, ax = plt.subplots(figsize=(10,6))

    # Define a list of line styles
    line_styles = ['-', '--', '-.', ':']

    # Define a color cycle (you can define your own list of colors here)
    color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Create a cycle for the colors that resets for each country
    country_color_cycle = itertools.cycle(color_cycle)

    indicator_names = []

    for country in countries:
        # Get the next color in the cycle
        country_color = next(country_color_cycle)

        # Create a cycle for the line styles that resets for each indicator
        line_style_cycle = itertools.cycle(line_styles)

        for indicator in indicators:
            df = get_world_bank_data(indicator, country, start_date, end_date)
            if not df.empty:
                # Get the next line style in the cycle
                line_style = next(line_style_cycle)

                # Get the name of the indicator from the DataFrame
                indicator_name = df['indicator'].iloc[0]
                if indicator_name not in indicator_names:
                    indicator_names.append(indicator_name)

                ax.plot(df.index, df['value'], label=f'{country} - {indicator_name}', linestyle=line_style, color=country_color)

    # Set the title to include the economic indicators
    ax.set_title(f'Economic Indicators from {start_date} to {end_date}')
    ax.set_xlabel('Year')

    # Set the y-axis label based on econ_format
    if econ_format == '%':
        ax.set_ylabel('Percentage of GDP')
    elif econ_format == 'US$':
        ax.set_ylabel('Current US$')
    else:
        ax.set_ylabel('Value')

    ax.legend(fontsize='small', bbox_to_anchor=(1.05, 1), loc='upper left')

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
        ax.yaxis.set_major_formatter(formatter)

    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)

    # Convert the buffer contents to base64 and return
    return base64.b64encode(buf.getbuffer()).decode("ascii")