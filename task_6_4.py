'''Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.'''


class Car:
    def __init__(self, name, color, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police: bool = is_police

    def go(self):
        return print(f' двигается прямо ')

    def stop(self):
        return print(f' остановился ')

    def turn(self, direction):
        return print(f' повернул {direction}')

    def show_speed(self):
        return print(f' скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            return print(f' превышает скорость на ', {int(self.speed) - 60}, f' км/ч')
        else:
            return print(f' скорость {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            return print(f' превышает скорость на ', {int(self.speed) - 40}, f' км/ч')
        else:
            return print(f' скорость {self.speed}')


class PoliceCar(Car):
    pass


my_auto = ['town_car Веста серебристая 55 False',
        'town_car Поло белая 60 False',
        'work_car Камаз желтый 35 False',
        'work_car Ивеко синий 40 False',
        'sport_car Феррари красный 100 False',
        'police_car Воронок белый 60 True']

city_auto = []

for count, line in enumerate(my_auto):
    type_auto, name, color, speed, is_police = line.split()
    if type_auto == 'town_car':
        city_auto.append(TownCar(name, color, speed, is_police))
    elif type_auto == 'sport_car':
        city_auto.append(SportCar(name, color, speed, is_police))
    elif type_auto == 'work_car':
        city_auto.append(WorkCar(name, color, speed, is_police))
    elif type_auto == 'police_car':
        city_auto.append(PoliceCar(name, color, speed, is_police))
    else:
        continue


while True:
    for count, line in enumerate(auto):
        random_move = random.randint(1, 3)
        if random_move == 1:
            setattr(auto[count], 'speed', 0)
            auto[count].stop()
        else:
            setattr(auto[count], 'speed', random.randint(5, 90))
        if random_move == 2:
            auto[count].go()
        elif random_move == 3:
            auto[count].turn('налево' if random.randint(1, 2) == 1 else 'направо')
        auto[count].show_speed()
        show_attr(auto[count])
        time.sleep(4)