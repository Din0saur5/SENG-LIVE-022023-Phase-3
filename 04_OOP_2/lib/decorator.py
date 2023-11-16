# 1. ✅ Demonstrate First Class Functions
    # Create functions to be used as callbacks 
    # Create a higher-order function that will take a callback as an argume

def feed(pet):
    return f'{pet} was fed.'

def walk(pet):
    return f'{pet} was walked'

# def taskForPet(func):
#     return func('rose')
# 2. ✅ Create a higher-order function that returns a function
# print(taskForPet(walk))

def taskForPet():
    def feed(pet):
        return f'{pet} was fed'
    return feed

# 3. ✅ Demonstrate a decorator
# Create a function that takes a function as an argument, has an inner function, and returns the inner function
# Demo examples of the decorator with and without pie syntax '@'
def coupon_calculation(func):
    def wrapper():
        print('base price $40')
        new_price = func(40.00)
        print(f'price with coupn ${new_price}')
    return wrapper

    # Without pie syntax 

def half_price(price):
    return '{:.2f}'.format(round(price/2,2)) 
#'{:.2f}' means to 2 decimal places format

half_off = coupon_calculation(half_price)
    # With pie syntax
@coupon_calculation
def five_less(price):
    return '{:.2f}'.format(round(price-5)) 