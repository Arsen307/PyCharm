import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = 'https://ua.sinoptik.ua/'
CITY = 'івано-франківськ'

# створюємо таблицю, якщо її не існує
conn = sqlite3.connect('Dz 10.sl3', 5)
c = conn.cursor()
c.execute("CREATE TABLE  temperature (datetime TEXT, temperature TEXT)")
conn.commit()

# отримуємо поточну температуру
response = requests.get(f"{URL}/погода-{CITY}")
soup = BeautifulSoup(response.content, 'html.parser')
temp = soup.find(class_='temperature').get_text()

# додаємо дані до бази даних
date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
c.execute("INSERT INTO temperature VALUES (?, ?)", (date_time, temp))
conn.commit()
conn.close()