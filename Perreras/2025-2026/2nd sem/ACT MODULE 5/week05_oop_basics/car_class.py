class Car_jbgp:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_car_jbgp(self):
        print(self.brand, self.model, self.year)

car1_jbgp = Car_jbgp("Toyota", "Corolla", 2020)
car1_jbgp.display_car_jbgp()

