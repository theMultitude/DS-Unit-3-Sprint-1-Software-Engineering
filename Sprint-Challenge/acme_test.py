import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 10)

    def test_stealability(self):
        """Test stealability() method."""
        test_arr = [1, 20, 200]
        s_arr = ["Not so stealable...", "Kinda stealable.", "Very stealable!"]
        for w in test_arr:
            prod = Product('Test Product', weight=w)
            self.assertEqual(prod.price, 10)

    def test_explode(self):
        """Test explode() method."""
        test_arr = [1, 20, 200]
        e_arr = ["...fizzle", "...boom!", "...BABOOM!"]
        for index in enumerate(test_arr):
            prod = Product('Test Product', weight=test_arr[index])
            self.assertEqual(prod.price, 10)

class AcmeReportTests(unitest.TestCase):
    def test_default_num_products(self):
        pass

    def test_legal_names(self):
        pass


if __name__ == '__main__':
    unittest.main()
