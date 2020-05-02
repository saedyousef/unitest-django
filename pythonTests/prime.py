import math

def is_prime(n):
    """ Detrmines if non-negative integer is prime. """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True