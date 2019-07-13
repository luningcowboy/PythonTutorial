from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Cat(Animal):
    def do_say(self):
        print('cat')

class Dog(Animal):
    def do_say(self):
        print('dog')

class AnimalFactory(object):
    def make_sound(self, obj_type):
        return eval(obj_type)().do_say()

if __name__ == '__main__':
    ff = AnimalFactory()
    animal = input('Whick animal Cat or Dog?')
    ff.make_sound(animal)
