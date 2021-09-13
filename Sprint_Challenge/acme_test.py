from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

def test_default_prod_price():
    prod = Product('Test Product')
    assert prod.price == 10

def test_default_prod_weight():
    prod = Product('Test Product')
    assert prod.weight == 20

def test_default_prod_flammability():
    prod = Product('Test Product')
    assert prod.flammability == 0.5

def test_stealability():
    prod = Product('Test Product', weight=0.5)
    assert prod.stealability() == 'Very stealable!'

def test_explode():
    prod = Product('Test Product', weight=100, flammability=100)
    assert prod.explode() == '...BABOOM!!'

def test_default_num_products():
    prod_list = generate_products()
    assert len(prod_list) == 30

def test_legal_names():
    prod_list = generate_products()
    for prod in prod_list:
        assert ' ' in prod.name
        split = prod.name.split()
        assert split[0] in ADJECTIVES
        assert split[1] in NOUNS