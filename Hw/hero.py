# 1)создать класс SuperHero с cвойством класса people='people'
class SuperHero:
    people = 'people'

# 2)создать конструктор класса(init) с атрибутами name,nickname,superpower,health_points,catchphrase.
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

# 3)создать метод который выводит имя героя
    def run(self):
        print(f'Name:{self.name}')

# 4)создать метод который умножает здоровье героя на 2
    def mul(self):
        print(f'health_points x 2:{self.health_points * 2}')

# 5) cоздать магический!! метод который выводит прозвище героя,его суперспособность и его здоровье
    def __str__(self):
        return f'Nickname:{self.nickname}\n' \
               f'SuperPower{self.superpower}\n' \
               f'Health_points:{self.health_points}'

# 6)создать магический!! метод который считает длину коронной фразы героя
    def __len__(self):
        return len(self.catchphrase)


# 7)создать объект класса Hero и применить все методы которые вы создали
Hero = SuperHero('Aang', 'Avatar', 'four_forces', 5, 'GoGo')

SuperHero.run(Hero)
SuperHero.mul(Hero)
print(Hero)
print(f'Lenght_catchphrase:{len(Hero)}')
