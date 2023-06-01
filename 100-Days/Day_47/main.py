import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
headers = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())
product_prices = soup.find(class_="a-price-whole").get_text()
# print(product_prices)
price_without_currency = product_prices.split("$")[0]
print(price_without_currency)
price_as_float = float(price_without_currency)
print(price_as_float)
