from fastapi import FastAPI, HTTPException,Response
import base64
import argparse
import uvicorn
from EcoStock.adalo import (
    candlestick, 
    bollinger_bands,
    correlation, 
    indicator_for_countries, 
    stock_correlation, 
    get_news,
    stock_prediction,
    portfolio_return
    )

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

@app.get("/correlation/{ticker}/{indicator}/{country}/{start_date}/{end_date}")
def correlation_api(ticker: str, indicator: str, country: str, start_date: str, end_date: str):
    try:
        # Generate the plot
        image = correlation(ticker, indicator, country, start_date, end_date)

        # Convert the base64 string back to bytes
        image_bytes = base64.b64decode(image)

        # Return a Response with the image data and the appropriate media type
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

@app.get("/bollinger_bands/{ticker}/{start_date}/{end_date}")
def bollinger_bands_api(ticker: str, start_date: str, end_date: str):
    try:
        # Generate the plot
        image = bollinger_bands(ticker, start_date, end_date)

        # Convert the base64 string back to bytes
        image_bytes = base64.b64decode(image)

        # Return a Response with the image data and the appropriate media type
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

@app.get('/indicator_for_countries/{indicator}/{countries}/{start_date}/{end_date}')
async def indicator_countries_api(indicator: str, countries: str, start_date: str, end_date: str):
    try:
        # Convert countries from string to list
        countries = countries.split(',')

        # Call the function and get the base64 encoded image
        image_base64 = indicator_for_countries(indicator, countries, start_date, end_date)

        # Convert the base64 string back to bytes
        image_bytes = base64.b64decode(image_base64)

        # Return a Response with the image data and the appropriate media type
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

@app.get("/get_news/{ticker}")
async def get_news_api(ticker: str):
    try:
        # Call the get_news function
        data = get_news(ticker)

        # Check if data is None (an error occurred)
        if data is None:
            raise HTTPException(status_code=400, detail="Error fetching news data")

        # Return the news data
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get('/stock_correlation/{tickers}/{start_date}/{end_date}')
async def stock_correlation_api(tickers: str, start_date: str, end_date: str):
    try:
        # Convert tickers from string to list
        tickers = tickers.split(',')

        # Call the function and get the base64 encoded image
        image_base64 = stock_correlation(tickers, start_date, end_date)

        # Convert the base64 string back to bytes
        image_bytes = base64.b64decode(image_base64)

        # Return a Response with the image data and the appropriate media type
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        return {"error": f"An error occurred: {e}"}
    
@app.get('/stock_prediction/{ticker}/{start_date}/{end_date}')
async def stock_prediction_api(ticker: str, start_date: str, end_date: str):
    try:
        
        # Call the function and get the base64 encoded image
        image_base64 = stock_prediction(ticker, start_date, end_date)

        # Convert the base64 string back to bytes
        image_bytes = base64.b64decode(image_base64)

        # Return a Response with the image data and the appropriate media type
        return Response(content=image_bytes, media_type="image/png")
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

@app.get('/portfolio_return/{tickers}/{start_date}/{end_date}')
async def portfolio_return_api(tickers: str, start_date: str, end_date: str):
    try:
        # Convert tickers from string to list
        tickers = tickers.split(',')

        # Call the function and get the base64 encoded image
        image_base64 = portfolio_return(tickers, start_date, end_date)

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
