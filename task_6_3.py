'''Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
(get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров.'''


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return str(self.name + ' ' + self.surname)

    def get_total_income(self):
        return int(self._income.get('wage')) + int(self._income.get('bonus'))


my_position = Position(f'{input("Введите имя сотрудника: ")}',
                       f'{input("Введите фамилию сотрудника: ")}', f''
                                                                   f'{input("Введите должность сотрудника: ")}',
                       {'wage': f'{input("Введите оклад сотрудника: ")}',
                        'bonus': f'{input("Введите премию сотрудника: ")}'})

print(f'Сотрудник: ', my_position.get_full_name(), f' c доходом = ', my_position.get_total_income(), ' рублей!')
