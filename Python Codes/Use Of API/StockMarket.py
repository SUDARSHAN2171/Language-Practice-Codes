import requests
from bs4 import BeautifulSoup

def fetch_stock_price(symbol):
    url = f"https://www.nseindia.com/get-quotes/equity?symbol={symbol}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find('div', {'class': 'stock-price'})
        if price_element:
            return float(price_element.text.strip().replace(',', ''))
        else:
            print(f"Could not find price data for {symbol}")
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
    return None