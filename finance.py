import yfinance as yf
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import threading
import time

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d", interval="1m")  # Fetch today's data
    return hist['Close']

def plot_stock_data(ticker):
    plt.ion()
    fig, ax = plt.subplots()
    
    while True:
        prices = fetch_stock_data(ticker)
        ax.clear()
        ax.plot(prices, label=f'{ticker} Price')
        ax.set_title(f'Stock Price of {ticker}')
        ax.set_xlabel('Time')
        ax.set_ylabel('Price (USD)')
        ax.legend()
        plt.draw()
        plt.pause(60)  # Update every 60 seconds

def check_price_alert(ticker, threshold):
    while True:
        current_price = fetch_stock_data(ticker).iloc[-1]
        if current_price >= threshold:
            messagebox.showinfo("Price Alert", f"{ticker} has reached {current_price} USD!")
        time.sleep(60)  # Check every 60 seconds

def start_monitoring():
    ticker = entry_ticker.get().upper()
    threshold = float(entry_threshold.get())
    threading.Thread(target=plot_stock_data, args=(ticker,), daemon=True).start()
    threading.Thread(target=check_price_alert, args=(ticker, threshold), daemon=True).start()

root = tk.Tk()
root.title("Stock Market Dashboard")

tk.Label(root, text="Enter Stock Ticker:").pack()
entry_ticker = tk.Entry(root)
entry_ticker.pack()

tk.Label(root, text="Set Price Alert:").pack()
entry_threshold = tk.Entry(root)
entry_threshold.pack()

tk.Button(root, text="Start Monitoring", command=start_monitoring).pack()

root.mainloop()
