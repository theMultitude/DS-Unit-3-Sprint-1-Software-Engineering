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
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        """Test stealability() method."""
        test_arr = [30, 18, 5]
        s_arr = ["Not so stealable...", "Kinda stealable.", "Very stealable!"]
        for i, item in enumerate(test_arr):
            prod = Product('Test Product', weight=test_arr[i])
            self.assertEqual(prod.stealability(), s_arr[i])

    def test_explode(self):
        """Test explode() method."""
        test_arr = [1, 20, 200]
        e_arr = ["...fizzle", "...boom!", "...BABOOM!"]
        for i, item in enumerate(test_arr):
            prod = Product('Test Product', weight=test_arr[i])
            self.assertEqual(prod.explode(), e_arr[i])

class AcmeReportTests(unittest.TestCase):
    """ Test that generate_products returns 30 resuts by default """
    def test_default_num_products(self):
        prods = generate_products()
        self.assertEqual(len(prods), 30)

    def test_legal_names(self):
        """ Tests if the names are in the appropriate format """
        prods = generate_products()
        for obj in prods:
            self.assertRegexpMatches(
            '(\w{2,10} \w{0,12}|\?{0,3}){1}', obj.name)


if __name__ == '__main__':
    unittest.main()
