import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0:3] = [dx*self.speed, dy*self.speed, dz*self.speed]


    def get_coords(self):
        print(self._cords)
        
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print(f"Sorry, i'm peaceful")
        else:
            print(F"Be careful, i'm attacking you 0_0")

    def speak(self):
        print(f'{self.sound}')

class Bird(Animal):
    beak = True

    def lay_eggs(self):
     i = random.randint(1,4)
     print(f'Here are(is) {i} eggs for you')

class AguaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self._cords[2] -= int(abs(dz)*self.speed/2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AguaticAnimal):
    sound = 'Click-click-click'
    def __init__(self, speed):
        super().__init__(speed)


db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1,2,3)
db.get_coords()
db.dive_in(6)
db.get_coords()

db.lay_eggs()

