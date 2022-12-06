import json;

class Product:
    def __init__(self, product = "", description = "", price = 0):
        self.product = product
        self.description = description
        self.price = price
    
    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self)-> str:
        return self.__str__()

if __name__ == "__main__":
    rez = Product(1, 2, 3)
    print(rez.__dict__)

