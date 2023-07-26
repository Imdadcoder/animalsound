class Animal:
    def make_sound(self):
        print("generic animal sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("bark")

class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("meow")

def animal_sound_in_zoo(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()

animal_sound_in_zoo(dog)
animal_sound_in_zoo(cat)