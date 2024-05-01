# Nell'init.py, puoi lasciarlo vuoto poiché non è necessario per il tuo progetto. 
# Tuttavia, è comune includere alcune informazioni sul pacchetto. Ecco un esempio di cosa potresti includere:          

"""
Economic-Finance Correlation Package

A Python package for investigating the correlation between economic and financial data.
"""

__version__ = "0.5.2"

from .api import app
from .adalo import (
    candlestick, 
    bollinger_bands,
    correlation, 
    indicator_for_countries, 
    stock_correlation, 
    get_news,
    stock_prediction,
    portfolio_return
)
from .functions import (
    get_stock_data,
    plot_candlestick,
    moving_avg_stock_data,
    get_world_bank_data,
    plot_correlation,
    plot_bollinger_bands,
    plot_indicator_for_countries,
    analyze_stock_correlation,
    plot_stock_prediction,
    plot_portfolio_return
)


# Questo file fornisce una breve descrizione del pacchetto e definisce la versione. 
# Infine, importa tutte le funzioni dal modulo functions.py in modo che siano disponibili quando importi il tuo pacchetto.