class Animal:
    def __init__ (self, Name=str, Age=int, Species=str):
        self.name=Name
        self.age=Age
        self.species=Species
    def print_info(self):
        print(f"name->{self.name}")
        print(f"age->{self.age}")
        print(f"species->{self.species}")


class Dog(Animal):
    def __init__ (self, Breed=str):
        self.breed=Breed
    def print_breed(self):
        print(f"breed->{self.breed}")

info_1=Animal("jaafar", 3, "Canis lupus familiaris")
info_2=Dog("german")
info_1.print_info()
info_2.print_breed()
print(30*"#")


class Cat(Animal):
    def __init__ (self, Color=str):
        self.color=Color
    def print_color(self):
        print(f"color->{self.color}")
        
info_1=Animal("semsem", 2, "Felis catus")
info_3=Cat("orange")
info_1.print_info()
info_3.print_color()