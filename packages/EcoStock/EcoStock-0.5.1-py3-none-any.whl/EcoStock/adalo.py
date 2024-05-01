import pandas as pd
import requests
import io
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import matplotlib.ticker as mticker
from statsmodels.tsa.arima.model import ARIMA
import warnings
import re
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

# Correlation between stock and economic data
def correlation(ticker, indicator, country, start_date, end_date):
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
    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)

    # Convert the buffer contents to base64 and return
    return base64.b64encode(buf.getbuffer()).decode("ascii")

# Bollinger Bands
def bollinger_bands(ticker, start_date, end_date):
    
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

# Economic indicator for countries
def indicator_for_countries(indicator, countries, start_date, end_date):
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
    
        # Determine the econ_format based on the econ_label
    if '$' in indicator_name:
        econ_format = 'US$'
    elif '%' in indicator_name:
        econ_format = '%'
    else:
        econ_format = None

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
def get_news(ticker):
    api_key = '8eb9080b292fef6aa96f1b6a78df86b9'
    url = f'https://gnews.io/api/v4/search?q={ticker}&token={api_key}&lang=en'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None

    try:
        data = response.json()
    except ValueError:
        print('Error parsing JSON response')
        return None

    # Prepare a list to hold the articles
    articles = []

    # Remove the number inside the brackets and append 'read more...' to the 'content' field for each article
    for article in data.get('articles', []):
        if 'content' in article:
            article['content'] = re.sub(r'\[\d+ chars\]', 'Click to read more...', article['content'])
            articles.append({
                'title': article.get('title'),
                'description': article.get('description'),
                'content': article.get('content'),
                'url': article.get('url'),
                'image': article.get('image'),
                'publishedAt': article.get('publishedAt'),
                'source': article.get('source', {}).get('name')
            })

    return articles

# Stock correlation
def stock_correlation(tickers, start_date, end_date):
    # Get the stock data
    stock_data = pd.DataFrame()
    for ticker in tickers:
        data = get_stock_data(ticker, start_date, end_date)
        stock_data[ticker] = data['Close']
    
    # Calculate daily returns in percentage
    returns = stock_data.pct_change() * 100
    
    # Create a figure and an axes with a smaller size
    fig, ax = plt.subplots(figsize=(8,4))

    # Plot the daily returns with thinner lines and transparency
    for ticker in tickers:
        ax.plot(returns.index, returns[ticker], label=ticker, linewidth=0.6, alpha=0.8)
    ax.set_title('Daily Returns of Stocks')
    ax.set_xlabel('Date')
    ax.set_ylabel('Daily Return (%)')

    # Add grid and legend with smaller font size
    ax.grid(True)
    ax.legend(fontsize='x-small')

    # Auto format date labels
    fig.autofmt_xdate()

    # Save the plot to a BytesIO object with a lower DPI
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)

    # Convert the buffer contents to base64 and return
    return base64.b64encode(buf.getbuffer()).decode("ascii")

# Stock prediction
def stock_prediction(ticker, start_date, end_date):
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

    # Create a figure
    fig, ax = plt.subplots(3, 1, figsize=(14, 8))
    
    # Plot the data
    ax[0].plot(full_data.index, full_data['Close'], label='Close Price')
    ax[0].plot(stock_data.index, stock_data['MA10'], label='10-day MA')
    ax[0].plot(stock_data.index, stock_data['MA50'], label='50-day MA')
    ax[0].plot(stock_data.index, stock_data['Upper Band'], label='Upper Bollinger Band')
    ax[0].plot(stock_data.index, stock_data['Lower Band'], label='Lower Bollinger Band')
    ax[0].plot(prediction_data.index, prediction_data['Close'], 'ro', label='Predicted Price')
    ax[0].set_title(f'{ticker} Stock Price Prediction: {prediction:.2f}$')
    ax[0].set_xlabel('Date')
    ax[0].set_ylabel('Price')
    ax[0].legend(fontsize='x-small')
    ax[0].grid(True)
    
    ax[1].plot(stock_data.index, stock_data['RSI'], label='RSI')
    ax[1].set_title('Relative Strength Index')
    ax[1].set_xlabel('Date')
    ax[1].set_ylabel('RSI')
    ax[1].legend(fontsize='x-small')
    ax[1].grid(True)
    
    ax[2].plot(stock_data.index, stock_data['MACD'], label='MACD')
    ax[2].plot(stock_data.index, stock_data['Signal Line'], label='Signal Line')
    ax[2].set_title('Moving Average Convergence Divergence')
    ax[2].set_xlabel('Date')
    ax[2].set_ylabel('MACD')
    ax[2].legend(fontsize='x-small')
    ax[2].grid(True)
    
    fig.autofmt_xdate()
    fig.tight_layout()

    # Save the plot to a BytesIO object with a lower DPI
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100)
    buf.seek(0)

    # Convert the buffer contents to base64 and return
    return base64.b64encode(buf.getbuffer()).decode("ascii")

# Portfolio return
def portfolio_return(tickers, start_date, end_date):
    """
    Calculate the overall return of a portfolio.

    Parameters:
    tickers (list): A list of ticker symbols.
    start_date (str): The start date in format 'yyyy-mm-dd'.
    end_date (str): The end date in format 'yyyy-mm-dd'.

    Returns:
    str: Base64 encoded string of the plot.
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

    # Create a new figure
    fig = plt.figure()

    # Plot the cumulative return
    plt.plot(portfolio_return.index, portfolio_return['Cumulative'])
    plt.title('Portfolio Cumulative Returns')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return (%)')

    # Auto format date labels
    fig.autofmt_xdate()

    # Save the plot to a BytesIO object with a lower DPI
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100)
    buf.seek(0)

    # Convert the buffer contents to base64 and return
    return base64.b64encode(buf.getbuffer()).decode("ascii")