import time

print("Зачекайте....")
time.sleep(2)
print("Майже готово....")

def timeit(self):
    def time_down(*args, **kwargs):
        start_chas = time.time()
        resultat = self(*args, **kwargs)
        time_is_end = time.time()
        result_time = round(time_is_end - start_chas, 2)
        print(f"Час виконання функції '{self.__name__}': \n{result_time} секунд")
        return resultat
    return time_down

@timeit
def my_time_function():
    time.sleep(3)
    print("Все готово!")
my_time_function()