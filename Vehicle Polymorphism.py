class Car:
    def __init__(self, brand, speed, price):
        self.brand = brand
        self.speed = speed
        self.price = price
    
    def get_details(self):
        return f"{self.brand}: Speed - {self.speed} km/h, Price - ${self.price}"
    
    def top_speed(self):
        return f"{self.brand}'s top speed is {self.speed} km/h"

def show_car_details(car):
    print(car.get_details())
    print(car.top_speed())


brand = input("Enter car brand: ")
speed = int(input("Enter car speed (km/h): "))
price = int(input("Enter car price ($): "))


user_car = Car(brand, speed, price)
show_car_details(user_car)

