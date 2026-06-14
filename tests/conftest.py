import pytest

@pytest.fixture
def correct_card_number():
    return '7000792289606361'

@pytest.fixture
def too_long_card_number():
    return '70007922896063612'

@pytest.fixture
def not_numeric_card_number():
    return '7000792289asdf606361'