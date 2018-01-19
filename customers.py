"""Customers at Hackbright."""

customer_dict = {}


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first, last, email, password):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about melon in console."""

        return "<{name}: {email}, {password}>".format(name=self.first_name + " " + self.last_name,
                                                      email=self.email, password=self.password)


def read_customer_info(path):
    """Read customer file and save to customer dictionary"""

    customer_file = open(path)
    for line in customer_file:
        customer_info = line.rstrip().split("|")
        customer = Customer(customer_info[0], customer_info[1],
                            customer_info[2], customer_info[3])
        customer_dict[customer_info[2]] = customer


def get_by_email(email):
    """Get customer object by email"""

    return customer_dict[email]
