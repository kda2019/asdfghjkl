# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return 3.14 * self.radius ** 2
#
#     def get_perimeter(self):
#         return 2 * 3.14 * self.radius
#
#     def set_radius(self, radius):
#         self.radius = radius
#
#
# '''
# Вивчити git, github
# '''
#
# def func(x, y):
#     p = x * y
#     return p


# class Car:
#     def __init__(self, name):
#         self.name = name
#         self.km = 0
#         self.fuel = 100
#         self.speed = 60
#
#     def ride(self, km):
#         self.km += km
#         self.fuel -= km / 10
#         return self.km
#
#
# class Kamaz(Car):
#
#     def __init__(self, name, kg=0):
#         super().__init__(name)
#         self.kg = 0
#
#     def take_some(self, kg):
#         self.kg += kg
#
#
# class AddFuelMixin:
#     def add_fuel(self, fuel):
#         self.fuel += fuel
#
#
# class FuelCar(Car, AddFuelMixin):
#     pass
#
#
# car = FuelCar('BMW')
#
#
# car.add_fuel(250)
#
# print(car.fuel)


class Hero:
    heroes = []
    chest = []

    def __init__(self, name):
        self.name = name
        self._hp = 100
        self.my_items = []
        self.damage = 10
        self.defence = 20
        Hero.heroes.append(self)

    def _get_total_damage(self, damage):
        return damage - self.defence

    def _get_damage(self, damage):
        self._hp -= self._get_total_damage(damage)

    def attack(self, enemy):
        enemy._get_damage(self.damage)

    def get_hp(self):
        return self._hp

    def __str__(self):
        return f"{self.name} - {self._hp}"

    def __repr__(self):
        return f"{self.name}"

    def __add__(self, other):
        self._hp += other
        return self

