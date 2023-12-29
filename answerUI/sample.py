class Sample:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price})"