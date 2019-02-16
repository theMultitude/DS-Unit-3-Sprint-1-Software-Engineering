import random
from acme import Product
from collections import defaultdict
from functools import reduce

products = []
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(n=30):
    count = n
    while(count > 0):
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0, 2.5)
        name = f'{random.choice(ADJECTIVES)} {random.choice(NOUNS)}'
        P = Product(name, price, weight, flammability)
        products.append(P)
        count -= 1
    return products

def inventory_report(arr):
    # identifying all the names created
    names = [arr[i].name for i in range(len(arr))]
    # using defaultdict to count unique names (products)
    IR = defaultdict(int)
    for name in names:
        IR[name] += 1

    print('Unique Products : ', len(IR))

    price = []
    weight = []
    flammability = []
    for dict in products:
        price.append(dict.price)
        weight.append(dict.weight)
        flammability.append(dict.flammability)

    def mean(arr):
        mean = reduce(lambda x, y: x+y, arr)/len(arr)
        return mean

    print('Average Price:', mean(price))
    print('Average Weight:', mean(weight))
    print('Average Price:', mean(flammability))

if __name__ == '__main__':
    inventory_report(generate_products())
