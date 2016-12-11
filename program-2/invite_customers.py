import math
import json


# Constants
EARTH_RADIUS = 6371 # km
DUBLIN_OFF_LAT_RAD = math.radians(53.3381985)
DUBLIN_OFF_LNG_RAD = math.radians(-6.2592576)


class Customer(object):

    def __init__(self, *args, **kwargs):
        self.customer_id = kwargs['user_id']
        self.name = kwargs['name']
        self.lng_rad = math.radians(float(kwargs['longitude']))
        self.lat_rad = math.radians(float(kwargs['latitude']))


    def get_customers_from_file():
        """
        Return all the customers listed in file
        """
        with open('customers.txt') as f:
            customers = []
            for line in f:
                dict_data = json.loads(line)
                customers.append(Customer(**dict_data))

            return sorted(customers, key=lambda k: k.customer_id)

    def calculate_distance_from_dublin_office(self):
        """
        Calculate distance of customer from intercom dublin office
        """

        delta_long = DUBLIN_OFF_LNG_RAD - self.lng_rad
        sines      = math.sin(self.lat_rad) * math.sin(DUBLIN_OFF_LAT_RAD)
        cosines    = math.cos(self.lat_rad) * math.cos(DUBLIN_OFF_LAT_RAD) * math.cos(delta_long)

        central_angle = math.acos(sines + cosines)
        distance      = EARTH_RADIUS * central_angle

        return distance

if __name__=='__main__':
    customers = Customer.get_customers_from_file()
    print('Invited Customers ID and Name are listed below:')
    print('-----------------------------------------------')
    for customer in customers:
        if customer.calculate_distance_from_dublin_office() <= 100:
            print("ID: {}, Name: {}".format(customer.customer_id, customer.name))