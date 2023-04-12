# Portfolio Optimizer API Documentation
The Portfolio Optimizer API provides an interface to optimize a portfolio of assets using a genetic algorithm. The API fetches historical stock price data from Alpha Vantage and optimizes the portfolio allocation to maximize the Sharpe ratio.

## Endpoints

### GET /
- Description: Returns a welcome message.
- Response: A welcome message.

### GET /favicon.ico
- Description: Returns the favicon for the API.
- Response: A FileResponse containing the favicon.

### POST /optimize_portfolio
- Description: Optimizes a portfolio based on the provided stock symbols, date range, and other parameters.
- Request Body:
    - stock_symbols (List[str]): A list of stock symbols to include in the portfolio.
    - start_date (str): The start date for the historical data (YYYY-MM-DD).
    - end_date (str): The end date for the historical data (YYYY-MM-DD).
    - pop_size (int, optional): The population size for the genetic algorithm (default: 100).
    - num_generations (int, optional): The number of generations for the genetic algorithm (default: 100).
    - risk_free_rate (float, optional): The risk-free rate used to calculate the Sharpe ratio (default: 0.02).
- Response:
    - allocation (Dict[str, float]): A dictionary containing the optimized asset allocation, with stock symbols as keys and their corresponding weights as values.
    - fitness (float): The fitness value (Sharpe ratio) of the optimized allocation.

- Examples
    - Get a welcome message
        ```
        curl http://127.0.0.1:8000
        ```
    - Optimize a portfolio
        ```
        curl -X POST -H "Content-Type: application/json" -d '{"stock_symbols": ["AAPL", "MSFT", "GOOGL"], "start_date": "2020-01-01","end_date": "2020-12-31"}' http://127.0.0.1:8000/optimize_portfolio
        ```
## Errors
- The API will return an appropriate HTTP status code and error message if there is an issue with the request or during the processing of the request. 
- Common errors include:
    - **400 Bad Request:** The request body is missing required fields or contains incorrect data.
    - **500 Internal Server Error:** An error occurred during the processing of the request, such as issues with fetching stock data.