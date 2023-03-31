import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 20 #(гроші у баксах $)
        self.alive = True
    def to_study(self):
        print("Time to study")
try:
        self.progress += gagsaf
        self.gladness -= 5
        self.money -= 3
except NameError:
    print("We have an NameError")
    print("Code after capsule")

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 5
    def make_money(self):
        print("Work time")
        self.gladness -= 2
        self.progress += 0.01
        self.money += 10
    def is_alive(self):
        logic_cube = random.randint(1, 2)
        if self.progress < -0.5:
            print("Case out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.money <= -10:
            print("You borrowed money and didn't pay it back, you're depressed...")
            self.alive = False
        #elif self.money < 0: #я спробував, але не працює код.
            #if logic_cube == 1:
                #self.make_money()
                #self.end_of_day()
                #self.is_alive()
        #elif self.progress < -0.2:
            #if logic_cube == 2:
                #self.to_study()
                #self.end_of_day()
                #self.is_alive()

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {round(self.money, 2)}")
    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 2:
            self.to_sleep()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 4:
            self.make_money()
            self.end_of_day()
            self.is_alive()

try:
    nick = Student(name="Nick")
    for day in range(365):
        if nick.alive == False:
            break
        nick.live(day)

except AttributeError:
    print("We have an AttributeError")