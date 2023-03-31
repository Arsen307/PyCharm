import colorama
import inspect

print("__name__:")
print(colorama.__name__) #Ім'я модулю
print(f"\n")

print("callable:")
print(callable(colorama)) #Перевіряє чи можна викликати дану колораму
print(f"\n")

print("dir:")
for check in dir(colorama): #Визначає вміст модулю
    print(check)
print(f"\n")

print("hasattr Fore:")
print(hasattr(colorama, "Fore")) #Fore(атрибут) дозволяє змінювати кольори тексту
#hassatr визначає чи є даний атрибут(Fore) у модулі
print(f"\n")

print("hasattr Style:")
print(hasattr(colorama, "Style")) #Style(атрибут) дозволяє змінювати стиль тексту(наприклад, жирний або курсивний)
#hassatr визначає чи є даний атрибут(Style) у модулі
print(f"\n")

print("inspect.ismodule:")
print(inspect.ismodule(colorama)) #Перевіряє чи colorama є модулем
print(f"\n")

print("inspect.isclass:")
print(inspect.isclass(colorama)) #Перевіряє чи colorama є класом
print(f"\n")

print("inspect.isfunction:")
print(inspect.isfunction(colorama)) #Перевіряє чи colorama є функцією
print(f"\n")

print("getmodule:")
print(inspect.getmodule(colorama)) #Де знаходиться модуль або звідки імпортований
print(f"\n")


