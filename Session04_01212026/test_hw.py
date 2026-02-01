# test_squares.py

def test_squares_of_even_numbers():
    expected = [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
    actual = squares_of_even_numbers()
    assert actual == expected, f"Fail: Expected {expected}, but got {actual}"
    print("Pass")

test_squares_of_even_numbers()