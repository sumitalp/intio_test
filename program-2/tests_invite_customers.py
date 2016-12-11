import unittest
from invite_customers import Customer


class TestInviteCustomer(unittest.TestCase):

    def test_method_exists(self):
        all_methods = dir(Customer)
        assert 'get_customers_from_file' in all_methods
        assert 'calculate_distance_from_dublin_office' in all_methods

    def test_init(self):
        customer_dict = {
            'user_id': 99,
            'name': 'Ahsan',
            'longitude': -9.442,
            'latitude': 51.802
        }

        new_customer = Customer(**customer_dict)

        self.assertEqual(customer_dict['user_id'], new_customer.customer_id)
        self.assertEqual(customer_dict['name'], new_customer.name)

    def test_get_customers_from_file(self):
        customers = Customer.get_customers_from_file()
        assert isinstance(customers[0], Customer)

        self.assertEqual(1, customers[0].customer_id)

    def test_calculate_distance_from_dublin_office(self):
        customer_1 = Customer(
            **{
                'user_id': 199, 'name': 'Customer One',
                'longitude': 15, 'latitude': 15
            }
        )

        customer_2 = Customer(
            **{
                'user_id': 299, 'name': 'Customer Two',
                'longitude': 0, 'latitude': 0
            }
        )

        self.assertEqual(4651,round(
            customer_1.calculate_distance_from_dublin_office()
        ))
        self.assertEqual(5959, round(
            customer_2.calculate_distance_from_dublin_office()
        ))

if __name__=='__main__':
    unittest.main()