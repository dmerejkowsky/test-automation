def add_four(x):
    return x + 5


def test_add_four_to_one_equals_five():
    actual = add_four(1)
    expected = 5
    assert actual == expected
