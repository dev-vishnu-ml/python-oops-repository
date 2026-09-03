# multiple inheritance concept
class Herbivore:
    plants_food = "grass and leaves"
    def eat_plants(self):
        print("eating only grass")

class Carnivore:
    Meat_food = "Fresh Meat"
    def eat_meat(self):
        print("eat only Meat")

class Omnivore:
    Mixed_food = "plants and Meat"
    def eat_both(self):
        print("eat both plants and meats")

class Bear(Herbivore, Carnivore, Omnivore):  #multiple inheritance
    pass

bear = Bear()
bear.eat_plants()
bear.eat_meat()
bear.eat_both()
print(f"Herbivore: {bear.plants_food}\nCarnivore:{bear.Meat_food}\nOmnivore: {bear.Mixed_food}")