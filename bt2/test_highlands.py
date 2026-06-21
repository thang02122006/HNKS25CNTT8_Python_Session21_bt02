import unittest

from main import (
    add_to_order,
    calculate_total,
    InvalidQuantityError,
    current_order
)


class TestHighlands(unittest.TestCase):

    def setUp(self):
        current_order.clear()

    def test_calculate_total(self):
        order = [
            {
                "code": "P1",
                "price": 35000,
                "quantity": 2
            },
            {
                "code": "F1",
                "price": 55000,
                "quantity": 1
            }
        ]
        result = calculate_total(order)
        self.assertEqual(result, 125000)
    def test_invalid_quantity(self):
        with self.assertRaises(InvalidQuantityError):
            add_to_order("P1", -1)

if __name__ == "__main__":
    unittest.main()