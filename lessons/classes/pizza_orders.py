"""Initiating A Class!"""

# import the class
# from <file_name>.<module_name> import <class>
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True)  # Constructor

# accessing/setting attributes
# my_pizza.size= "large"
# my_pizza.toppings = 10
# my_pizza.gluten_free = True

# printing out some values

# print("my_pizza: ")
# print(my_pizza)

print("Pizza:")
print(Pizza)

print("Size attribute: ")
print(my_pizza.size)

print("Toppings: ")
print(my_pizza.toppings)

# sals_pizza size medium, 5 toppings, not gluten free
sals_pizza: Pizza = Pizza("mediun", 5, False)


def price(inp_pizza: Pizza) -> float:
    """Given a pizza, calculate the price of that pizza."""
    if inp_pizza.size == "large":
        price: float = 6.25
    else:
        price: float = 5.00
    price += .75 * inp_pizza.toppings
    if inp_pizza.gluten_free:
        price += 1.00
    return price


# calling price function
print(price(sals_pizza))
print(price(my_pizza))

# calling price method
print(sals_pizza.price())
print(my_pizza.price())

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(2)
print(my_other_pizza.toppings)
print(my_pizza.toppings)
