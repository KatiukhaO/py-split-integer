from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    assert sum(split_integer(8, 1)) == 8


def test_value_split_into_equal_parts_when_value_is_div_by_number_of_parts():
    assert split_integer(6, 2) == [3, 3]


def test_should_return_a_part_equals_to_a_value_when_slitting_into_one_part():
    assert split_integer(9, 1) == [9]


def test_parts_should_be_sorted_when_they_are_not_equal():
    assert split_integer(17, 4) == sorted(split_integer(17, 4))


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
