class ShopInventory:
    def __init__(self,products:list):
        self.products = products
    
    def display(self):
        print(f"\n{'ID':>5} {'Name':>20} ${'Price':>8} {'Qty':>5}")
        print("-"*50)
        for p in self.products:
            print(f"{p[0]:>5} {p[1]:>20} ${p[2]:>8} {p[3]:>5}")
    
    def search(self):
        pro_name = input("Enter the product name: ").strip().lower()
        found = [p for p in self.products if pro_name in p[1].lower()]
        if found:
            for p in found:
                print(f" {p[0]} | {p[1]} | ${p[2]:.2f} | Qty:{p[3]}")
        else:
            print(f"{pro_name} was not found.")

    def lowstock(self,threshold=5):
        low = [p for p in self.products if p[3]<threshold]
        if low:
            for p in low:
                print(f" {p[1]}: only {p[3]} left")
        else:
            print("All item well stocked.")

    def value(self):
        return sum(p[2] * p[3] for p in self.products)
    
    def restock(self):
        try:
            self.pro_id = int(input("Enter product id to restock: "))
            self.quantity = int(input("How many to add: "))

            for i,p in enumerate(self.products):
                if p[0] == self.pro_id:
                    self.products[i] = (p[0], p[1], p[2], p[3]+self.quantity)
                    print(f"Updated! {p[1]} is now restocked and now {p[3]+self.quantity} in stock.")
                    break
                else:
                    print("Product id not found.")
        except ValueError:
            print("Please enter a valid numbers.")

    
    def run(self):
        while True:
            print("\n1.View Inventory 2.Search 3.Low Stock 4.Value 5.Restock 6.Exit")
            print()
            choice = input("What you want to check: ")

            if choice == "1": 
                self.display()
            elif choice == "2": 
                self.search()
            elif choice == "3": 
                self.lowstock()
            elif choice == "4": 
                total_val = self.value()
                print(f"Total Inventory value: ${total_val:.2f}")
            elif choice == "5": 
                self.restock()
            elif choice == "6": 
                break
            else: 
                print("Invalid Option.")
    
            again = input("Back to the option? Y/N: ")
            again = again.strip().lower()

            if again == "n":
                print("To check the inventory again run py inventory_opp.py")
                break

Inventory = ShopInventory([
(101, "Notebook", 2.50, 20),
(102, "Pen Set", 4.99, 3),
(103, "USB Cable", 8.00, 12),
(104, "Mouse Pad", 6.50, 2),
(105, "Stapler", 9.99, 15),
])

Inventory.run()