class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} makes a {self.sound} sound.")

class Dog(Animal):
    def __init__(self, name, sound, breed):
        Animal.__init__(self, name, sound)
        self.breed = breed

    def info(self):
        print(f"{self.name} is a {self.breed} and it barks.")

class Cat(Animal):
    def __init__(self, name, sound, color):
        Animal.__init__(self, name, sound)
        self.color = color

    def info(self):
        print(f"{self.name} is a {self.color} cat and it meows.")

dog = Dog("Buddy", "bark", "Golden Retriever")
cat = Cat("Whiskers", "meows", "black")

dog.make_sound()
dog.info()

cat.make_sound()
cat.info()

# try:
#     print("나누기 전용  계산기입니다.")
#     num1 = float(input("첫번째 숫자를 입력하세요 : "))   # 정수만 받을 수 있음
#     num2 = float(input("두번재 숫자를 입력하세요 : "))
#     print(f"{num1} / {num2} = {float(num1) / num2}")
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)


import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)

import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

import glob
print(glob.glob("*.py"))

import os
print(os.getcwd())

folder = "sample_dir"
if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")
print(os.listdir())

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은 " + str(today + td))

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [3, 1, 4]
z = [3, 2, 3]
plt.plot(x, y)
plt.show()

import numpy as np
# option = "cos"
# option = "sin"
# option = "exp"
# option = "line"
option = "ln"

def y():
    global option
    if option=="sin":
        x = np.linspace(0, 3*np.pi, 100)
        return x, np.sin(x)
    elif option=="cos":
        x = np.linspace(-np.pi, 2 * np.pi, 100)
        return x, np.cos(x)
    elif option=="line":
        x = np.linspace(0, 5, 100)
        return x, 3 * x + 2
    elif option=="exp":
        x = np.linspace(-5, 5, 100)
        return x, np.exp(x)
    elif option=="ln":
        x = np.linspace(0, 10, 100)
        return x, np.log(x)
    else:
        x = np.linspace(0, 100, 100)
        return x, x

if __name__ == "__main__":
    plt.plot(*y())
    plt.grid(True)
    plt.show()
