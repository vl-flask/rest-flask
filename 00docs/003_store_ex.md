# Static and Class Methods - Exercise

The code in the exercise. 
```python
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return cls(store.name + " - franchise")
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        return f"{store.name}, total stock price: {int(store.stock_price())}"
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'

store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)
print(store2.items)
franchise1 = Store.franchise(store)
franchise2 = Store.franchise(store2)
print(franchise1.name)
print(franchise2.name)
print(Store.store_details(store))
print(Store.store_details(store2))
```
