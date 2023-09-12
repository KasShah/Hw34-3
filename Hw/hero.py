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
        print(f'Name: {self.name}')

    # 4)создать метод который умножает здоровье героя на 2
    def mul(self):
        print(f'health_points x 2: {self.health_points * 2}')

    # 5) cоздать магический!! метод который выводит прозвище героя,его суперспособность и его здоровье
    def __str__(self):
        return f'Nickname: {self.nickname}\n' \
               f'SuperPower: {self.superpower}\n' \
               f'Health_points: {self.health_points}'

    # 6)создать магический!! метод который считает длину коронной фразы героя
    def __len__(self):
        return len(self.catchphrase)


# 7)создать объект класса Hero и применить все методы которые вы создали
Hero = SuperHero('Aang', 'Avatar', 'four_forces', 10, 'GoGo')

SuperHero.run(Hero)
print(Hero)
SuperHero.mul(Hero)
print(f'Lenght_catchphrase: {len(Hero)}')


class AirHero(SuperHero):
    fly = False

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def mul(self):
        print(f'health_points **2: {self.health_points ** 2}')
        if self.health_points ** 2:
            print(f'{self.fly} = {True}')

    def phrase(self):
        print('True in the True_phrase')


airhero = AirHero('Gyatso', 'Monk', 'Wisdom', 3, 'White Lotus', 9)

AirHero.run(airhero)
print(airhero)
AirHero.mul(airhero)
print(f'Damage: {airhero.damage}')
AirHero.phrase(airhero)


class EarthHero(SuperHero):
    fly = False

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage

    def mul(self):
        print(f'health_points **2: {self.health_points ** 2}')
        if self.health_points ** 2:
            print(f'{self.fly} = {True}')

    def phrase(self):
        print('True in the True_phrase')


earthhero = EarthHero('Saad', 'Master', 'Earth magic', 5, 'Stone block', 9)

EarthHero.run(earthhero)
print(earthhero)
EarthHero.mul(earthhero)
print(f'Damage: {earthhero.damage}')
EarthHero.phrase(earthhero)


class Vilian(AirHero):
    people = 'monster'

    def gen_x(self): ...

    def crit(self):
        print(f'damage ** 2: {self.damage ** 2}')


vilian = Vilian('Azai', 'Lord_of_Fire', 'Lightning', 10, "I'm the Phoenix King", 8)

print(vilian.crit())
