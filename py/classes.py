# class Coordinate():
#     def __init__(self, input_x, input_y):
#         self.x = input_x
#         self.y = input_y

# p = Coordinate(3, 4)
# print(f"This is the x value -> {p.x}")
# print(f"This is the y value -> {p.y}")

# # New Object dont have "new" keyword
# # self is like "this" in Java, a ref to the object itself
# # self is the first parameter of every method in a class
# # Dot natation to get instance variables
# # __init__ is a constructor, what happens when you create a new object


# # DEMO

# class Flight():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []
    
#     def add_passenger(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True

#     def open_seats(self):
#         return self.capacity - len(self.passengers)


# Ksm_Nrb = Flight(5)

# people = ["Tom", "Jerry", "Mickey", "Donald", "Goofy", "Pluto"]

# for p in people:
#     valid = Ksm_Nrb.add_passenger(p)
#     if valid:
#         print(f"Added {p} to the flight successfully.")
#     else:
#         print(f"No available seats for {p}")


# DEMO 2
class Category():
    def __init__(self, name, items):
        self.n = name
        self.items = [items]
        self.check_categories()

    def add_categories(self):
        for c in categories:
            if self.n == c:
                c.items.append(self.items)
        
    def check_categories(self):
        if self.n not in categories:
            categories.append(self.n)

class Product():
    def __init__(self, name, quantity, price, category):
        self.n = name
        self.q = quantity
        self.p = price
        self.c = category
        self.add_products()

    def add_products(self):
        Category(self.c, self.n)
        products.append({self.n : [self.q, self.p, self.c]})
        



categories = []

products = []

demo  = Product("Tissue", 2, 40, "Toiletries")
demo2 = Product("Toothpaste", 10, 200, "Toiletries")
demo3 = Product("CoCacola", 12, 60, "Drinks")

print(f"{products} -> products")
print(f"{categories} -> categories")