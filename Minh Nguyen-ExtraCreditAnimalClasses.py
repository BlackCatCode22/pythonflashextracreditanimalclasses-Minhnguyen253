# Extra Credit Animal Class
# CIT-95 Python SP23
# Minh Nguyen 0920131
# 03/26/2023
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old")


class Lion(Animal):
    def __init__(self, name, age, weigh):
        super().__init__(name, age)
        self.weigh = weigh

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and My weigh is {self.weigh} lbs.")

    def speak(self):
        print("Brother, help me!.....Long live the King!")


class Hyena(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and My color is {self.color} color.")

    def speak(self):
        print("Hahaha That's how I laugh/sound.")


l = Lion("Mufasa", 6, 450)
l.show()
l.speak()
print()
h = Hyena("Shenzi", 4, "tan")
h.show()
h.speak()
