
# My Python Snippets 🐍

A collection of reusable Python functions and snippets for various projects. Handy utilities for data processing, automation, and general coding tasks

## 📂 Files in this Repository

### 1️⃣ fetch_weather_data.ipynb 🌦️
**Description:**  
This Jupyter Notebook contains functions to fetch weather data from (https://www.wunderground.com/) API and process it into a structured format for further analysis.
Get your own API key

### 2️⃣ mysql_connector.ipynb, mysql_connector.py🛢️
**Description:**  
This notebook provides a MySQL connection utility using SQLAlchemy and Pandas. It includes functions to establish database connections and fetch data seamlessly.

### 3️⃣ track_daily_changes_wh_operations.ipynb 📊
**Description:**  
A script to track daily changes in warehouse operations, providing insights into stock movements and operational trends.

### 4️⃣ read_silo.ipynb
**Description:** 
This script reads a CSV file using **pandas** and performs basic data cleaning by removing single quotes (`'`) from all string values in the DataFrame. The cleaned data is then displayed using `.head()`.

### 5️⃣ extract_shipment_info.ipynb
**Description:** 
This script **connects to a MySQL database**, extracts **filtered and grouped shipment records**, and **exports the cleaned data to CSV files**. The extracted data is useful for tracking **freight amounts, shipment weight, and scheduled deliveries**.
With a simple line chart

### 6️⃣ get_ticker_data.ipynb
**Description:**
A Python function to fetch historical market data and financial statements for a given stock using the Yahoo Finance API (yfinance).

📌 Features
✅ Retrieve historical market data (Open, High, Low, Close, Volume)
✅ Get balance sheets for a stock
✅ Fetch quarterly income statements
✅ Uses logging for debugging and error handling
✅ Handles invalid tickers gracefully


---

## 🚀 Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/TW168/my-python-snippets.git
