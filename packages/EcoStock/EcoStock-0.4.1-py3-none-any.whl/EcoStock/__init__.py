# Nell'init.py, puoi lasciarlo vuoto poiché non è necessario per il tuo progetto. 
# Tuttavia, è comune includere alcune informazioni sul pacchetto. Ecco un esempio di cosa potresti includere:          

"""
Economic-Finance Correlation Package

A Python package for investigating the correlation between economic and financial data.
"""

__version__ = "0.4.1"

from .api import app
from .adalo import (
    candlestick,
    indicator_for_countries,
    get_news,
    comparison_indicators_countries,
    bollinger_bands
)
from .functions import (
    get_stock_data,
    plot_candlestick,
    moving_avg_stock_data,
    get_world_bank_data,
    plot_correlation,
    plot_bollinger_bands,
    plot_indicator_for_countries,
    compare_indicators_countries
)


# Questo file fornisce una breve descrizione del pacchetto e definisce la versione. 
# Infine, importa tutte le funzioni dal modulo functions.py in modo che siano disponibili quando importi il tuo pacchetto.