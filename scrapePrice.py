import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver


url = "https://www.amazon.com"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

chromeDriverPath = r'C:\Users\Rorozo\Documents\Code\chromedriver.exe'



response = requests.get(url, headers=header)



soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(id="kindle-price-column").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)