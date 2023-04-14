import datetime

now = datetime.datetime.now()
print("Поточна дата і час: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

from bs4 import BeautifulSoup
import requests

def bitcoin(self):

    def wrapper(*args, **kwargs):
        response = requests.get("https://coinmarketcap.com/")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, features="html.parser")
            soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
            res = soup_list[0].find("span")
            print(res.text)
        return self(*args, **kwargs)
    return wrapper

@bitcoin
def my_function():
    print("This is bitcoin exchange rate.")

my_function()