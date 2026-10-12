# 1. Créer et utiliser une classe
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.__age = age          # attribut privé (deux underscores)

    def get_age(self):
        return self.__age

    def sit(self):
        print(self.name + " is now sitting")

    def roll_over(self):
        print(self.name + " rolled over!")

    def shout(self):
        print("Dog shouts")


dog = Dog("Husky", 2)
print(dog.name)
print(dog.get_age())
dog.sit()
dog.roll_over()


# 2. Héritage
class Husky(Dog):
    pass

mydog = Husky("Larry", 3)
print(mydog.name)
print(mydog.get_age())


# 3. Polymorphisme : on redéfinit shout() dans les sous-classes
class Husky2(Dog):
    def shout(self):
        print("woo")

class Tibetan_Mastiff(Dog):
    def shout(self):
        print("barking")

def sound(d):
    d.shout()

sound(Husky2("Larry", 3))
sound(Dog("Richard", 2))
sound(Tibetan_Mastiff("Sylvia", 4))