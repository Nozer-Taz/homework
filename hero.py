

class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    
    def say_my_name(self):
        return f'My name is {self.name}'
    
    def health_multiply(self):
        return self.health_points * 2

    def __str__(self):
        return f'Hero: {self.nickname}, superpower: {self.superpower}, health: {self.health_points}'

    def __sizeof__(self):
        return f'Catchphrase length: {len(self.catchphrase)}'


class CosmoHero(SuperHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    @property
    def who_am_i(self):
        return f'I am {self.nickname}, my catchphrase is - {self.catchphrase}'
    
    def health_multiply(self):
        self.health_points **= 2
        self.fly = True
        return self.health_points, self.fly
    
    def true_phrase(self):
        return 'True in the True_phrase'


class AeroHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False
    
    @property
    def who_am_i(self):
        return f'I am {self.nickname}, my catchphrase is - {self.catchphrase}'

    def health_multiply(self):
        self.health_points **= 2
        self.fly = True
        return self.health_points, self.fly


    def true_phrase(self):
        return 'True in the True_phrase'


cos_hero = CosmoHero('Cosmos', 'Univa', 'Black hole creation', 50, 'Ahah Lol, catch a black hole', 10)

aer_hero = AeroHero('Aang', 'Avatar', 'Avatar experience', 60, 'Please don\'t bully me', 20)

print(cos_hero.true_phrase())
print(cos_hero.health_points)
print(cos_hero.health_multiply())
print(cos_hero.health_points)
print(cos_hero.who_am_i)

print(aer_hero.true_phrase())
print(aer_hero.health_points)
print(aer_hero.health_multiply())
print(aer_hero.health_points)
print(aer_hero.who_am_i)


class Villain(CosmoHero):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
    
    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 1.5
        return self.damage

vill1 = Villain('Zuko', 'Blue demon', 'Fire bender', 100, 'I will restore my honor', 55)
vill2 = Villain('Azula', 'Crazy', 'Fire bending', 120, 'My mother called me a monster', 60)

print(vill2.crit())
