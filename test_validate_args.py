import pytest


@pytest.mark.smoke
def test_validate_args__int_input(calculator):
    assert calculator.validate_args(3, 5) is None


@pytest.mark.smoke
def test_validate_args__float_input(calculator):
    assert calculator.validate_args(1.4, -1.8) is None


@pytest.mark.smoke
def test_validate_args__complex_input(calculator):
    assert calculator.validate_args(complex(2, 4), complex(3, 5)) is None


@pytest.mark.regression
def test_validate_args__mixed_valid_inputs(calculator):
    assert calculator.validate_args(3, complex(3, 5)) is None
    assert calculator.validate_args(1.4, complex(3, 5)) is None
    assert calculator.validate_args(3, 1.4) is None


@pytest.mark.smoke
def test_validate_args__bool_input(calculator):
    with pytest.raises(ValueError):
        calculator.validate_args(True, False)


@pytest.mark.smoke
def test_validate_args__str_input(calculator):
    with pytest.raises(ValueError):
        calculator.validate_args('str', 'str')


@pytest.mark.smoke
def test_validate_args__set_input(calculator):
    with pytest.raises(ValueError):
        calculator.validate_args({1, 2, 3}, {2, 3})


@pytest.mark.regression
def test_validate_args__frozenset_input(calculator):
    with pytest.raises(ValueError):
        calculator.validate_args(frozenset({1, 2}), frozenset({3, 4}))


@pytest.mark.regression
def test_validate_args__dict_input(calculator):
    with pytest.raises(ValueError):
        calculator.validate_args({1: 'a'}, {2: 'b'})


@pytest.mark.regression
def test_validate_args__list_input(calculator):
    with pytest.raises(ValueError):
        calculator.validate_args([1, 2], [3, 4])


@pytest.mark.regression
def test_validate_args__tuple_input(calculator):
    with pytest.raises(ValueError):
        calculator.validate_args((1, 2), (3, 5))


@pytest.mark.nightly
def test_validate_args__mixed_invalid_inputs(calculator):
    invalid_args = [True, 'str', {1, 2}, 
                    frozenset({1, 3}), {1: 'a'}, [1, 2], (1, 2)]
    for first in range(len(invalid_args)):
        for second in range(first + 1, len(invalid_args)):
            print(f'pair: {invalid_args[first]}:{invalid_args[second]}')
            with pytest.raises(ValueError):
                assert calculator.validate_args(invalid_args[first], 
                                                invalid_args[second])
