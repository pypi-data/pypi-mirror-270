from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from io import BytesIO
import base64
import argparse
import uvicorn
from EcoStock.functions import (
    get_stock_data,
    moving_avg_stock_data,
    get_world_bank_data,
    plot_correlation
)
from EcoStock.adalo import (
    candlestick, 
    bollinger_bands, 
    indicator_for_countries, 
    comparison_indicators_countries, 
    get_news)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"results": {
    "message": "Welcome to EcoStock API!"
  }}

@app.get("/candlestick/{ticker}/{start_date}/{end_date}")
async def candlestick_api(ticker: str, start_date: str, end_date: str):
    """
    Fetch the stock data and plot it as a simple line chart.

    Parameters:
    ticker (str): Ticker symbol of the stock.
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.
    """
    try:
        # Fetch the stock data and plot
        fig = candlestick(ticker, start_date, end_date)

        # Check if fig is a Figure instance
        if fig:
            # Save the plot to a BytesIO object
            buf = BytesIO()
            fig.savefig(buf, format="png")
            buf.seek(0)
            
            # Convert the buffer contents to base64 and create a data URL
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            return JSONResponse(content={"image": f"data:image/png;base64,{data}"})
        else:
            return {"error": "No data available or an error occurred"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

@app.get("/plot_correlation/{ticker}/{start_year}/{end_year}/{indicator}/{country}/{start_date}/{end_date}/{econ_label}/{econ_format}")
async def plot_correlation_api(ticker: str, start_year: str, end_year: str, indicator: str, country: str, start_date: str, end_date: str, econ_label: str, econ_format: str = None):
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
    try:
        # Fetch the stock data and plot
        fig = plot_correlation(ticker, start_year, end_year, indicator, country, start_date, end_date, econ_label, econ_format)

        # Check if fig is a Figure instance
        if fig:
            # Save the plot to a BytesIO object
            buf = BytesIO()
            fig.savefig(buf, format="png")
            buf.seek(0)
            
            # Convert the buffer contents to base64 and create a data URL
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            return JSONResponse(content={"image": f"data:image/png;base64,{data}"})
        else:
            return {"error": "No data available or an error occurred"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

@app.get("/bollinger_bands/{ticker}/{start_date}/{end_date}/{window_size}/{num_of_std}")
async def bollinger_bands_api(ticker: str, start_date: str, end_date: str, window_size: int, num_of_std: int):
    try:
        fig = bollinger_bands(ticker, start_date, end_date, window_size, num_of_std)
        
        # Check if fig is a Figure instance
        if fig:
            # Save the plot to a BytesIO object
            buf = BytesIO()
            fig.savefig(buf, format="png")
            buf.seek(0)
            
            # Convert the buffer contents to base64 and create a data URL
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            return JSONResponse(content={"image": f"data:image/png;base64,{data}"})
        else:
            return {"error": "No data available or an error occurred"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

@app.get("/indicator_for_countries/{indicator}/{countries}/{start_date}/{end_date}")
async def indicator_for_countries_api(indicator: str, countries: str, start_date: str, end_date: str):
    """
    Fetch the economic indicator data for several countries and plot it.

    Parameters:
    indicator (str): The indicator of interest.
    countries (str): The countries of interest, separated by commas.
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.
    """
    try:
        # Convert the countries string to a list
        countries_list = countries.split(',')

        # Fetch the data and plot
        fig = indicator_for_countries(indicator, countries_list, start_date, end_date)

        # Check if fig is a Figure instance
        if fig:
            # Save the plot to a BytesIO object
            buf = BytesIO()
            fig.savefig(buf, format="png")
            buf.seek(0)
            
            # Convert the buffer contents to base64 and create a data URL
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            return JSONResponse(content={"image": f"data:image/png;base64,{data}"})
        else:
            return {"error": "No data available or an error occurred"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

@app.get("/get_news/{symbol}")
async def get_news_api(symbol: str):
    try:
        # Call the get_news function
        data = get_news(symbol)

        # Check if data is None (an error occurred)
        if data is None:
            raise HTTPException(status_code=400, detail="Error fetching news data")

        # Return the news data
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/comparison_indicators_countries/{indicators}/{countries}/{start_date}/{end_date}")
async def comparison_indicators_countries(indicators: str, countries: str, start_date: str, end_date: str):
    """
    Fetch the comparison plot for given indicators and countries.

    Parameters:
    indicators (str): The indicators of interest, separated by commas.
    countries (str): The countries of interest, separated by commas.
    start_date (str): The start date for the data.
    end_date (str): The end date for the data.
    """
    try:
        # Split the indicators and countries strings into lists
        indicators_list = indicators.split(",")
        countries_list = countries.split(",")

        # Fetch the comparison plot
        fig = comparison_indicators_countries(indicators_list, countries_list, start_date, end_date)
        
        if fig:
            # Save the plot to a BytesIO object
            buf = BytesIO()
            fig.savefig(buf, format="png")
            buf.seek(0)
            
            # Convert the buffer contents to base64 and create a data URL
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            return JSONResponse(content={"image": f"data:image/png;base64,{data}"})
        else:
            return {"error": "No data available or an error occurred"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Run the FastAPI application.")
    parser.add_argument("-p", "--port", type=int, default=8000, help="The port to bind.")
    parser.add_argument("-r", "--reload", action="store_true", help="Enable hot reloading.")
    args = parser.parse_args()

    uvicorn.run("api:app", host="127.0.0.1", port=args.port, reload=args.reload)
