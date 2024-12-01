# Made by: Marwan Amr Mohamed
class animal:
    def __init__(self,n):
        self._name = n
    def eat(self):
        print(f"{self._name} is Eating, wait for him to Finish")
    def sleep(self):
        print(f"{self._name} is Sleeping, Leave him in Peace")

class dog(animal):
    def __init__(self,n):
        super().__init__(n)
    def bark(self):
        print(f"{self._name} is Barking, HOOF HOOF")

class cat(animal):
    def __init__(self,n):
        super().__init__(n)
    def meow(self):
        print(f"{self._name} is Meowing, MEOW MEOW")

a = animal("bla")
c = cat("Mos3ad")
d = dog("Hambozo")
c.meow()
c.eat()
c.sleep()
print("-----------------")
d.bark()
d.eat()
d.sleep()



