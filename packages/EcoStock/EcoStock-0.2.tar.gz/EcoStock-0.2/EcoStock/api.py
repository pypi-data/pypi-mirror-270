from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os
import plotly.io as pio
import traceback
import argparse
import sys
import uvicorn
from typing import List
from typing import Optional
from EcoStock.functions import (
    get_stock_data,
    plot_candlestick,
    moving_avg_stock_data,
    get_world_bank_data,
    plot_correlation,
    plot_bollinger_bands,
    get_news,
    plot_indicator_for_countries,
    compare_indicators_countries
)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"results": {
    "message": "Welcome to EcoStock API!"
  }}

@app.get("/stock_data/{ticker}/{start_date}/{end_date}")
async def get_stock_data_api(ticker: str, start_date: str, end_date: str):
    try:
        data = get_stock_data(ticker, start_date, end_date).to_dict(orient='records')
        return JSONResponse(content={
            "status": "success",
            "message": "Stock data fetched successfully",
            "ticker": ticker,
            "start_date": start_date,
            "end_date": end_date,
            "results": data
        })
    except Exception as e:
        return JSONResponse(content={
            "status": "error",
            "message": str(e),
        }, status_code=400)

# Mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

def ensure_static_dir():
    # Create the 'static' directory if it doesn't exist
    if not os.path.exists('static'):
        os.makedirs('static')

@app.get("/plot_candlestick/{ticker}/{start_date}/{end_date}")
async def plot_candlestick_api(ticker: str, start_date: str, end_date: str):
    try:
        # Generate the plot
        fig = plot_candlestick(ticker, start_date, end_date)

        # Create the 'static' directory if it doesn't exist
        if not os.path.exists('static'):
            os.makedirs('static')

        # Save the figure as a PNG image
        image_path = f"static/{ticker}_{start_date}_{end_date}.png"
        pio.write_image(fig, image_path)

        # Return the image URL
        return {"url": f"https://ecofin-496487b9809a.herokuapp.com/{image_path}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/moving_avg_stock_data/{ticker}/{start_year}/{end_year}")
async def moving_avg_stock_data_api(ticker: str, start_year: str, end_year: str):
    try:
        # Call the moving_avg_stock_data function
        df = moving_avg_stock_data(ticker, start_year, end_year)

        # Convert the DataFrame to a dictionary and return it as a JSON response
        return JSONResponse(content={
            "status": "success",
            "message": "Moving average stock data fetched successfully",
            "ticker": ticker,
            "start_year": start_year,
            "end_year": end_year,
            "results": df.to_dict(orient='records')
        })
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/world_bank_data/{indicator}/{country}/{start_date}/{end_date}")
async def world_bank_data_api(indicator: str, country: str, start_date: str, end_date: str):
    try:
        # Call the get_world_bank_data function
        df = get_world_bank_data(indicator, country, start_date, end_date)

        # Convert the DataFrame to a dictionary and return it as a JSON response
        return JSONResponse(content={
            "status": "success",
            "message": "World Bank data fetched successfully",
            "indicator": indicator,
            "country": country,
            "start_date": start_date,
            "end_date": end_date,
            "results": df.to_dict(orient='records')
        })
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/plot_correlation/{ticker}/{start_year}/{end_year}/{indicator}/{country}/{start_date}/{end_date}/{econ_label}/{econ_format}")
async def plot_correlation_api(ticker: str, start_year: str, end_year: str, indicator: str, country: str, start_date: str, end_date: str, econ_label: str, econ_format: str = None):
    try:
        # Call the plot_correlation function
        plot_correlation(ticker, start_year, end_year, indicator, country, start_date, end_date, econ_label, econ_format)

        # Create the 'static' directory if it doesn't exist
        if not os.path.exists('static'):
            os.makedirs('static')

        # Save the current figure as an image file in the 'static' directory
        image_path = f"static/{ticker}_{indicator}.png"
        plt.savefig(image_path)

        # Close the current figure to free up memory
        plt.close()

        # Return the image URL
        return {"url": f"https://ecofin-496487b9809a.herokuapp.com/{image_path}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/plot_bollinger_bands/{ticker}/{start_date}/{end_date}/{window_size}/{num_of_std}")
async def plot_bollinger_bands_api(ticker: str, start_date: str, end_date: str, window_size: int, num_of_std: int):
    try:
        # Call the plot_bollinger_bands function
        fig = plot_bollinger_bands(ticker, start_date, end_date, window_size, num_of_std)

        # Create the 'static' directory if it doesn't exist
        if not os.path.exists('static'):
            os.makedirs('static')

        # Save the current figure as an image file in the 'static' directory
        image_path = f"static/{ticker}_bollinger_bands.png"
        fig.write_image(image_path)

        # Return the image URL
        return {"url": f"https://ecofin-496487b9809a.herokuapp.com/{image_path}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

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

@app.get("/plot_indicator_for_countries/{indicator}/{start_date}/{end_date}")
async def plot_indicator_for_countries_api(indicator: str, countries: List[str], start_date: str, end_date: str):
    try:
        # Call the plot_indicator_for_countries function
        fig = plot_indicator_for_countries(indicator, countries, start_date, end_date)

        # Create the 'static' directory if it doesn't exist
        if not os.path.exists('static'):
            os.makedirs('static')

        # Save the current figure as an image file in the 'static' directory
        image_path = f"static/{indicator}_for_countries.png"
        fig.write_image(image_path)

        # Return the image URL
        return {"url": f"https://ecofin-496487b9809a.herokuapp.com/{image_path}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/compare_indicators_countries/{start_date}/{end_date}")
async def compare_indicators_countries_api(indicators: List[str], countries: List[str], start_date: str, end_date: str):
    try:
        # Call the compare_indicators_countries function
        fig = compare_indicators_countries(indicators, countries, start_date, end_date)

        # Create the 'static' directory if it doesn't exist
        if not os.path.exists('static'):
            os.makedirs('static')

        # Save the current figure as an image file in the 'static' directory
        image_path = f"static/compare_indicators_countries.png"
        fig.write_image(image_path)

        # Return the image URL
        return {"url": f"https://ecofin-496487b9809a.herokuapp.com/{image_path}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Run the FastAPI application.")
    parser.add_argument("-p", "--port", type=int, default=8000, help="The port to bind.")
    parser.add_argument("-r", "--reload", action="store_true", help="Enable hot reloading.")
    args = parser.parse_args()

    uvicorn.run("api:app", host="127.0.0.1", port=args.port, reload=args.reload)
