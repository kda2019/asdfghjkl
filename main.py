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

