class Animal():
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        print(self.name,"likes to",self.sound)
    

class Dog(Animal):
    def speak(self):
        print(self.name,"likes to Bark")
    
    def fetch(self):
        print(self.name,"go fetch")
    

class Cat(Animal):
    def speak(self):
        print(self.name,"likes to meow")


d1 = Dog("Rocky","Bark")
c1 = Cat("Melody","Meow")

d1.fetch()
d1.speak()
c1.speak()
