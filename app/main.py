from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse
from typing import List
from app.ga_solver import ga_solver
from app.utils import fetch_alpha_vantage_data
from pydantic import BaseModel
import pandas as pd

import logging
from fastapi.logger import logger as fastapi_logger

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Use FastAPI's logger for Uvicorn logs
uvicorn_logger = logging.getLogger("uvicorn")
fastapi_logger.handlers = uvicorn_logger.handlers
fastapi_logger.setLevel(uvicorn_logger.level)


app = FastAPI()


@app.get("/")
def read_root():
    logger.info("Welcome to the Portfolio Optimizer API")
    return {"message": "Welcome to the Portfolio Optimizer API"}


@app.get("/favicon.ico")
def read_favicon():
    logger.info("Returning favicon.ico")
    return FileResponse("favicon.ico")

class PortfolioOptimizationRequest(BaseModel):
    stock_symbols: List[str]
    start_date: str
    end_date: str
    pop_size: int = 100
    num_generations: int = 100
    risk_free_rate: float = 0.02

@app.post("/optimize_portfolio")
async def optimize_portfolio(req: PortfolioOptimizationRequest):
    # Fetch historical stock price data for each symbol
    logger.info("Fetching stock data")
    stock_data = {}
    for symbol in req.stock_symbols:
        stock_data[symbol] = fetch_alpha_vantage_data(
            symbol, req.start_date, req.end_date)
        
    # Combine the data into a single DataFrame
    combined_data = pd.concat(
        stock_data.values(), axis=1, keys=stock_data.keys())
    returns = combined_data.pct_change().dropna()

    # GA solver for portfolio optimization
    best_allocation, best_fitness = ga_solver(returns, req.pop_size, req.num_generations, req.risk_free_rate)

    # Format the results for the response
    result = {
        "allocation": {symbol: weight for symbol, weight in zip(req.stock_symbols, best_allocation)},
        "fitness": best_fitness
    }

    # # Return a dummy response for testing
    # result = {
    #     "stock_data": stock_data,
    #     "returns": returns.to_dict()
    # }
    
    logger.info(f"Returning result: {result}")
    return result
