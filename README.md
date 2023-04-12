# Portfolio Optimizer:
This project implements a distributed genetic algorithm (GA) for portfolio optimization, using Python, FastAPI, and Dask. 
The application fetches historical stock price data from Alpha Vantage and optimizes the portfolio allocation to maximize the Sharpe ratio. 
The frontend communicates with the backend via a simple REST API to send input data and receive optimization results.

## Application Structure:
The app directory contains the following files and folders:

```
portfolio_optimizer/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── ga_solver.py
│   ├── portfolio.py
│   ├── utils.py
│   └── config.py
│
├── tests/
│   ├── __init__.py
│   ├── test_ga_solver.py
│   └── test_portfolio.py
│
├── requirements.txt
└── README.md
```

## app/
- **__init__.py:** Empty file to mark the app directory as a Python package.

- **main.py:** The entry point for the FastAPI application. Sets up the API routes and handles incoming requests. It uses the Portfolio class from `portfolio.py` and the `ga_solver` function from `ga_solver.py` to perform the portfolio optimization. Additionally, it fetches historical stock price data using the utility function `fetch_alpha_vantage_data` from `utils.py`.

- **ga_solver.py:** Contains the distributed GA solver for portfolio optimization using Dask. Defines the GA components, such as representation, initialization, fitness function, selection, crossover, and mutation, and provides the main `ga_solver` function. The `main.py` file imports the `ga_solver` function and uses it to perform the portfolio optimization.

- **portfolio.py:** Contains the Portfolio class, which represents a portfolio of assets. It takes asset weights and historical returns as inputs and provides methods to calculate the expected return, risk, and Sharpe ratio of the portfolio. The `main.py` file creates an instance of this class and uses its methods to evaluate the performance of the optimized portfolio.

- **utils.py:** Contains utility functions, such as `fetch_alpha_vantage_data`, which fetches historical stock price data from Alpha Vantage. The `main.py` file imports this function to retrieve historical price data for the given stock symbols.

- **config.py:** Defines configuration variables for the application, such as API keys for fetching stock price data and any other required settings. The `main.py` and `utils.py` files import these settings to configure the API calls and other aspects of the application.

## tests/
- **__init__.py:** Empty file to mark the tests directory as a Python package.

- **test_ga_solver.py:** Contains unit tests for the GA solver components, such as initialization, selection, crossover, and mutation. Additionally, it can test the overall GA solver with a known problem to verify its correctness.

- **test_portfolio.py:** Contains unit tests for the Portfolio class, ensuring that the expected_return, risk, and sharpe_ratio methods work correctly.

## Setup and Installation

- Clone the repository and navigate to the project directory.

- Create a virtual environment and activate it:

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

- Install the required packages:

    ```
    pip install -r requirements.txt
    ```

- Set up the environment variables:

    ```
    export ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
    
    Replace your_alpha_vantage_api_key
    ```




    