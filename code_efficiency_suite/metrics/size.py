from pympler import asizeof


def measure_size(obj):
    """
    Μετράει το πραγματικό μέγεθος ενός αντικειμένου στη RAM.
    Επιστρέφει bytes.
    Χρησιμοποιεί το pympler.asizeof για ακριβή recursive μέτρηση.
    """
    return asizeof.asizeof(obj)
