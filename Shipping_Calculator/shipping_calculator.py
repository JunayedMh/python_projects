class ShippingCalculator:
    def __init__(self,zone:str,weight:float,speed:str):
        self.zone = zone.strip().capitalize()
        self.weight = weight
        self.speed = speed.strip().capitalize()
        self.cost = 0
    
    def calculate_dest_rate(self):
        if self.zone == "Domestic":
            self.cost = 5
        elif self.zone == "Continental":
            self.cost = 15
        elif self.zone == "International":
            self.cost = 30
        else:
            print("Please enter correct destination.")
            return False
        return True
    
    def calculate_extra_weight_p(self):
        if self.weight > 5:
            extra_weight = self.weight - 5
            if self.zone == "International":
             self.cost = self.cost + extra_weight * 5
            else:
                self.cost = self.cost + extra_weight * 2
    
    def apply_speed_price(self):
        if self.speed == "Regular":
            self.cost = self.cost
        elif self.speed == "Express":
            self.cost = self.cost + self.cost * 20/100
        elif self.speed == "Overnight":
            self.cost = self.cost + self.cost * 50/100
        else:
            print("Warning! Please enter a valid option.")

    def maximum_cap(self):
        if self.zone == "International" and self.cost > 200:
            self.cost = 200
    
    def final_cost(self):
        if not self.calculate_dest_rate():
            return 0.0
        
        self.calculate_extra_weight_p()
        self.apply_speed_price()
        self.maximum_cap()
        return round(self.cost, 2)
    

print("..........Global Shipping Price Engine........")

user_zone = input("Enter destination (Domestic / Continental / International): ")
user_weight = float(input("Enter package weight in kg: "))
user_speed = input("Delivery speed (Regular / Express / Overnight): ")

calculator = ShippingCalculator(zone=user_zone,weight=user_weight,speed=user_speed)
final_price = calculator.final_cost()
if final_price > 0:
        print("." * 40)
        print(f"Final shipping cost: ${final_price:.2f}")
