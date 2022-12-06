from product import Product
import json

class Department:
    def __init__(self, nameD = "", products = []):
        self.nameD = nameD
        self.products = products
        self.__dict__["products"] = [i.__dict__ for i in self.products] 
    
    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self)-> str:
        return self.__str__()

if __name__ == "__main__":
    rez = Department(1, [Product(1, 2, 3), Product(1, 2, 3)])
    print(rez.__dict__)
