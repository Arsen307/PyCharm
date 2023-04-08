import requests
import datetime

now = datetime.datetime.now()
print("Поточна дата і час: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

response = requests.get("https://ua.sinoptik.ua/погода-івано-франківськ")
print(response.text)


from bs4 import BeautifulSoup
import requests
response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
    res = soup_list[0].find("span")
    print(res.text)