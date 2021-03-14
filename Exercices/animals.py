class Dog:
    # Set class level variable
    scientific_name = "Canis lupus familiaris"

    # Set instance variable
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Woof!")

    def eat(self, food):
        if food == "biscuit":
            print("Yummy!")
        else:
            print("I want a biscuit!")

    # def learn_name(self, name):
    #     self.name = name

    def hear(self, words):
        if self.name in words:
            self.speak()

    def do_trick(self):
        pass


class Chihuahua(Dog):
    pass
    origin = "Mexico"

    def speak(self):
        print("Yip!")


class TrainedChihuahua(Chihuahua):
    def do_trick(self):
        print(f"{self.name} spins in the air!")


class Husky(Dog):
    origin = "Siberia"

    def speak(self):
        print("Awooo!")
