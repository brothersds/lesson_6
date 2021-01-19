'''Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.'''

import random
import time


class Car:
    def __init__(self, name, color, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police: bool = is_police

    def go(self):
        return print(f'двигается прямо ')

    def stop(self):
        return print(f'остановился ')

    def turn(self, direction):
        return print(f'повернул {direction}')

    def show_speed(self):
        return print(f'скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            return print(f'превышает скорость на ', int(self.speed) - 60, f' км/ч')
        else:
            return print(f'скорость {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            return print(f'превышает скорость на ', int(self.speed) - 40, f' км/ч')
        else:
            return print(f'двигается со скоростью {self.speed}')


class PoliceCar(Car):
    pass


def show_attr(auto_obj):
    return (f"Автомобиль {getattr(auto_obj, 'name')} {getattr(auto_obj, 'color')} цвета "
            f"это {getattr(auto_obj, 'is_police')}-полиция")


my_auto = ['town_car Веста серебристого 65 False',
           'town_car Поло белого 0 False',
           'work_car Камаз желтого 0 False',
           'work_car Ивеко синего 0 False',
           'sport_car Феррари красного 0 False',
           'police_car Воронок белого 0 True']

city_auto = []
for count, line in enumerate(my_auto):
    type_auto, a_name, a_color, a_speed, a_police = line.split()
    if type_auto == 'town_car':
        city_auto.append(TownCar(a_name, a_color, a_speed, a_police))
    elif type_auto == 'sport_car':
        city_auto.append(SportCar(a_name, a_color, a_speed, a_police))
    elif type_auto == 'work_car':
        city_auto.append(WorkCar(a_name, a_color, a_speed, a_police))
    elif type_auto == 'police_car':
        city_auto.append(PoliceCar(a_name, a_color, a_speed, a_police))
    else:
        continue

while True:
    for count, line in enumerate(city_auto):
        print(show_attr(city_auto[count]))
        random_move = random.randint(1, 3)
        if random_move == 1:
            setattr(city_auto[count], 'speed', 0), city_auto[count].stop()
        elif random_move == 2:
            city_auto[count].go(), setattr(city_auto[count], 'speed', random.randint(15, 100))
        elif random_move == 3:
            city_auto[count].turn('налево' if random.randint(1, 2) == 1 else 'направо')
            setattr(city_auto[count], 'speed', random.randint(15, 100))
        else:
            continue
        city_auto[count].show_speed()
        print(53 * '-')
        time.sleep(3)
