class Product:
    product_range = 0

    def __init__(self, name: str, price: float, quantity: float):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.product_range += 1

    def change_quantity(self, count: float) -> bool:
        if self.quantity + count >= 0:
            self.quantity += count
            print(f"New numbers of {self.name} in stock: {self.quantity}")
            return True
        else:
            print("Not enought product in stock!")
            return False

    def set_price(self, new_price: float) -> bool:
        if type(new_price) != float or type(new_price) != int:
            print("Price must be real number!")
            return False
        
        if new_price < 0:
            print("Price cannot be less than 0!")
            return False
        else:
            self.price = new_price
            print(f"New price for product {self.name}: {self.price}")
            return True

    def set_quantity(self, new_quantity: float) -> bool:
        if type(new_quantity) != float or type(new_quantity) != int:
            print("Quantity must be real number!")
            return False
        
        if new_quantity < 0:
            print("Quantity cannot be less than 0!")
            return False
        else:
            self.quantity = new_quantity
            print(f"New numbers of product in stock: {self.quantity}")
            return True

    def get_name(self) -> str:
        return self.name
    
    def get_price(self) -> float:
        return self.price

    def get_quantity(self) -> float:
        return self.quantity

    def get_info(self) -> str:
        return f"{self.name};{self.price};{self.quantity}\n"

    @classmethod
    def get_product_range(cls) -> int:
        return cls.product_range
    
    @classmethod
    def product_remove(cls):
        cls.product_range -= 1