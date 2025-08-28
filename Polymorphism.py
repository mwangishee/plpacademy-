class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

class Boat:
    def move(self):
        return "Sailing 🚤"

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
