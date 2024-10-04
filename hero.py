

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
    

hero1 = SuperHero(name='Bruce', nickname='Batman', superpower='will power', health_points=100, catchphrase='You either die a hero or live long enough to see yourself become the villain')

print(hero1.say_my_name())
print(hero1.health_multiply())
print(hero1.__str__())
print(hero1.__sizeof__())