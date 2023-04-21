
                                          #ТЕМА: ПАРСИНГ САЙТУ З БІРЖОЮ КРИПТИ
import datetime

now = datetime.datetime.now() #Цей рядок коду отримує поточну дату та час з операційної системи,
                            #зберігає їх у змінну now та форматує їх у строку за допомогою методу strftime

print("Поточна дата і час: ")
print(now.strftime("%Y-%m-%d %H:%M:%S")) #Цей рядок коду виводить поточну дату та час
                                        #у форматі року-місяця-дня години:хвилини:секунди за допомогою методу strftime

#STRFTIME - це метод, який перетворює об'єкт дати або часу на рядок згідно з заданим форматом

from bs4 import BeautifulSoup
import requests

def crypta(self):

    def wrapper(*args, **kwargs): #Обгортка виконує запит до веб-сторінки "https://coinmarketcap.com/" та отримує її вміст у форматі HTML
        #*args позиційний параметр, **kwargs іменнований параметр

        response = requests.get("https://coinmarketcap.com/") #Створює запит веб-сторінки
        if response.status_code == 200: #Чи успішно виконанно запит?

            soup = BeautifulSoup(response.text, features="html.parser")
            #Представляє HTML код сторінки та вказує парсер який буде використовуватись для аналізу

            soup_list1 = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
            #Знаходить усі посилання <a> з атрибутом href рівним "/currencies/bitcoin/markets/" та повертає список цих елементів

            res1 = soup_list1[0].find("span") #Знаходить перший елемент списку та шукає в ньому перший елемент з тегом <span>

            Bitcoin = "Bitcoin"

            print(f"{Bitcoin:=^50}" f"\n", "Price:", res1.text)#Виводить та форматує рядки

            #Аналогічно за цим принципом виводить інші валюти

            soup_list2 = soup.find_all("a", {"href": "/currencies/ethereum/markets/"})
            res2 = soup_list2[0].find("span")
            Ethereum = "Ethereum"
            print(f"{Ethereum:=^50}" f"\n", "Price:", res2.text)


            soup_list3 = soup.find_all("a", {"href": "/currencies/tether/markets/"})
            res3 = soup_list3[0].find("span")
            Tether = "Tether"
            print(f"{Tether:=^50}" f"\n", "Price:", res3.text)


            soup_list4 = soup.find_all("a", {"href": "/currencies/bnb/markets/"})
            res4 = soup_list4[0].find("span")
            BNB = "BNB"
            print(f"{BNB:=^50}" f"\n", "Price:", res4.text)


            soup_list5 = soup.find_all("a", {"href": "/currencies/usd-coin/markets/"})
            res5 = soup_list5[0].find("span")
            Usd_Coin = "Usd-Coin"
            print(f"{Usd_Coin:=^50}" f"\n", "Price:", res5.text)


            soup_list6 = soup.find_all("a", {"href": "/currencies/xrp/markets/"})
            res6 = soup_list6[0].find("span")
            XRP = "XRP"
            print(f"{XRP:=^50}" f"\n", "Price:", res6.text)


            soup_list7 = soup.find_all("a", {"href": "/currencies/cardano/markets/"})
            res7 = soup_list7[0].find("span")
            Cardano = "Cardano"
            print(f"{Cardano:=^50}" f"\n", "Price:", res7.text)


            soup_list8 = soup.find_all("a", {"href": "/currencies/dogecoin/markets/"})
            res8 = soup_list8[0].find("span")
            Dogecoin = "Dogecoin"
            print(f"{Dogecoin:=^50}" f"\n", "Price:", res8.text)


            soup_list9 = soup.find_all("a", {"href": "/currencies/polygon/markets/"})
            res9 = soup_list9[0].find("span")
            Polygon = "Polygon"
            print(f"{Polygon:=^50}" f"\n", "Price:", res9.text)


            soup_list10 = soup.find_all("a", {"href": "/currencies/solana/markets/"})
            res10 = soup_list10[0].find("span")
            Solana = "Solana"
            print(f"{Solana:=^50}" f"\n", "Price:", res10.text)
            Dorivnuje = "="
            print(f"{Dorivnuje:=^50}")
        return self(*args, **kwargs) #викликає оригінальну функцію з переданими їй аргументами *args та **kwargs і повертає результат її виконання
    return wrapper #Повертає функцію обгортки для використання декоратору

@crypta #Декоратор
def my_function():
    print("           THIS IS CRYPTA EXCHANGE RATE")

my_function() #Викликає функцію

