from prime import is_prime

def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"Error on is_prime({n}), expected {expected} ")
    else:
        print(f"is_prime({n}) passed the test Successfully!")
        