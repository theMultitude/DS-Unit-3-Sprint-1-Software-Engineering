import random
from acme import Product
from collections import defaultdict

products = []
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(n=30):
    while(n > 0):
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flamability = random.uniform(0, 2.5)
        name = random.choice(ADJECTIVES) + " " + random.choice(NOUNS)
        P = Product(name, price, weight, flamability)
        products.append(P)
        n =- n

    return products

def inventory_report(arr):
    IR = defaultdict(int)
    for product in products:
        IR[product] += 1
