class Item:
    def __init__(self,name:str,price:float,quantity=0) -> None:
        self.name=name
        self.price=price
        self.quantity = quantity
        print(f"Created")
        pass
    
    def calculate(self):
        return self.price * self.quantity

item1 = Item("Laptop",1000,2.5)
print(f"{item1.name}  {item1.price}")
print(f"{item1.calculate()}")
# item1.