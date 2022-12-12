from product import Product
from department import Department
import json

class Store:
    def __init__(self, number = "", address = "", departments = []):
        self.number = number
        self.address = address
        self.departments = departments
        self.__dict__["departments"] = [i.__dict__ for i in self.departments]
    
    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self)-> str:
        return self.__str__()

def StoreSerialize(Store, path):
    with open(path, 'w') as outfile:
        json.dump(Store.__dict__, outfile, indent=4, ensure_ascii = False)
        

def StoreDeserialize(pas):
    def Decode(obj):
        if "departments" in obj:
            return Store(obj["number"], obj["address"], [Decode(i) for i in obj["departments"]])
        elif "products" in obj:
            return Department(obj["nameD"], [Decode(i) for i in obj["products"]])
        else:
            return Product(obj["product"], obj["description"],obj["price"])
    with open(pas) as json_file:
        data = json.load(json_file)
    return Decode(data)


if __name__ == "__main__":
    rez = Store(1, "2", [Department(1, [Product(1, 2, 3), Product(1, 2, 3)]), Department(1, [Product(1, 2, 3), Product(1, 2, 3)])])
    print(rez.__dict__)

