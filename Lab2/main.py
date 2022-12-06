import json
from product import Product
from department import Department
from store import Store, StoreSerialize, StoreDeserialize

firstStore = Store("1", "Kuybisheva. 22", 
                [Department("Clothes", [
                    Product("1", "2", "1000"),
                    Product("2","4", "800"),
                    Product("3","9", "1200"),
                    Product("4","16","500")]),
                Department("Boots", [
                    Product("1", "38", "2000"),
                    Product("2","44", "10000"),
                    Product("3","28","1800"),
                    Product("4","42","3350")])])

StoreSerialize(firstStore, "firstS.json")
secondStore = StoreDeserialize("firstS.json")

print(secondStore.__dict__)