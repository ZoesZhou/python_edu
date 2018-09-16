from t2 import Person
from t3 import get_score


def monkey_patch_4_person():
    Person.get_score = get_score


monkey_patch_4_person()  # 打补丁

if __name__ == '__main__':
    print(Person().get_score())
    print(Person.__dict__)
    print(get_score.__dict__)


# class Car:
#     def __init__(self, mark='BMW', color='Black', price='2000$', speed='120km/h'):
#         self.__mark = mark
#         self.__color = color
#         self.__price = price
#         self.__speed = speed
#
#     def get_info(self):
#         return self.__dict__  # 用filter过滤不需要的信息
#
#
# class CraInfo:
#     # cars = []
#     def __init__(self):
#         self.cars = []
#
#     def add_car(self, car: Car):
#         self.cars.append(car)
#
#     def get_all_car_info(self):
#         pass
