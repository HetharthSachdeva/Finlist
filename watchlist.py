import yfinance as yf

def get_stock_data(watchlist):
    stock_data = []
    for stock in watchlist:
        try:
            data = yf.Ticker(stock)
            Info = data.info
            History = data.history(period='1d', interval='1m')
            stock_data.append({
                'symbol': Info.get('longName'),
                'price': round((History.iloc[-1])['Close'],2),
                'open': Info.get('open'),
                'p_close': Info.get('previousClose')
            })
        except Exception as e:
            continue    
    return stock_data

def add_to_watchlist(stock_symbol, watchlist):
    if stock_symbol not in watchlist:
        watchlist.append(stock_symbol)
