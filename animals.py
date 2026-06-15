class Animal():
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        print("Animal Noise")
    

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name,"Bark")
    
    def speak(self):
        print("Bark")

    def fetch(self):
        print(self.name,"fetch ")
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name,"Meow")

    def speak(self):
        print("Meow")


d1 = Dog("Rocky")
c1 = Cat("Melody")

d1.fetch()
d1.speak()
c1.speak()
print(c1.name)
print(d1.name)

