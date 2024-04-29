from fastapi import FastAPI, HTTPException,Response
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
    correlation, 
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
def candlestick_api(ticker: str, start_date: str, end_date: str):
    try:
        # Generate the plot
        image = candlestick(ticker, start_date, end_date)

        # Convert the base64 string back to bytes
        image_bytes = base64.b64decode(image)

        # Return a Response with the image data and the appropriate media type
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

@app.get("/correlation/{ticker}/{start_year}/{end_year}/{indicator}/{country}/{start_date}/{end_date}/{econ_label}/{econ_format}")
def correlation_api(ticker: str, start_year: str, end_year: str, indicator: str, country: str, start_date: str, end_date: str, econ_label: str, econ_format: str = None):
    try:
        # Generate the plot
        image = correlation(ticker, start_year, end_year, indicator, country, start_date, end_date, econ_label, econ_format)

        # Convert the base64 string back to bytes
        image_bytes = base64.b64decode(image)

        # Return a Response with the image data and the appropriate media type
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

@app.get("/bollinger_bands/{ticker}/{start_date}/{end_date}/{window_size}/{num_of_std}")
def bollinger_bands_api(ticker: str, start_date: str, end_date: str, window_size: int, num_of_std: int):
    try:
        # Generate the plot
        image = bollinger_bands(ticker, start_date, end_date, window_size, num_of_std)

        # Convert the base64 string back to bytes
        image_bytes = base64.b64decode(image)

        # Return a Response with the image data and the appropriate media type
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

@app.get('/indicator_for_countries/{indicator}/countries/{countries}/start_date/{start_date}/end_date/{end_date}/econ_format/{econ_format}')
async def indicator_countries_api(indicator: str, countries: str, start_date: str, end_date: str, econ_format: str = None):
    try:
        # Convert countries from string to list
        countries = countries.split(',')

        # Call the function and get the base64 encoded image
        image_base64 = indicator_for_countries(indicator, countries, start_date, end_date, econ_format)

        # Convert the base64 string back to bytes
        image_bytes = base64.b64decode(image_base64)

        # Return a Response with the image data and the appropriate media type
        return Response(content=image_bytes, media_type="image/png")
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

@app.get('/comparison_indicators_countries/indicators/{indicators}/countries/{countries}/start_date/{start_date}/end_date/{end_date}/econ_format/{econ_format}')
async def comparison_indicators_countries_api(indicators: str, countries: str, start_date: str, end_date: str, econ_format: str = None):
    try:
        # Convert indicators and countries from string to list
        indicators = indicators.split(',')
        countries = countries.split(',')

        # Call the function and get the base64 encoded image
        image_base64 = comparison_indicators_countries(indicators, countries, start_date, end_date, econ_format)

        # Convert the base64 string back to bytes
        image_bytes = base64.b64decode(image_base64)

        # Return a Response with the image data and the appropriate media type
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        return {"error": f"An error occurred: {e}"}
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Run the FastAPI application.")
    parser.add_argument("-p", "--port", type=int, default=8000, help="The port to bind.")
    parser.add_argument("-r", "--reload", action="store_true", help="Enable hot reloading.")
    args = parser.parse_args()

    uvicorn.run("api:app", host="127.0.0.1", port=args.port, reload=args.reload)
