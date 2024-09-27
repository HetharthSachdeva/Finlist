from flask import Flask, render_template, request, redirect
import yfinance as yf
from watchlist import get_stock_data, add_to_watchlist

app = Flask(__name__)

# Watchlist of default stocks
watchlist = ["^NSEI", "^NSEBANK", "^CNXFMCG", "^MIDCPNIFTY"]

@app.route('/')
def home():
    stock_data = get_stock_data(watchlist)
    return render_template('home.html', stock_data=stock_data)

@app.route('/add', methods=['POST'])
def add_stock():

    stock_symbol = request.form.get('stock_symbol')
    stock_symbol = (stock_symbol).upper() + '.NS'
    add_to_watchlist(stock_symbol, watchlist)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
