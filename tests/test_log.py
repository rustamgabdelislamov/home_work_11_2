import pytest

from decorators.log import log
from src.masks import get_mask_card_number


@log("log.txt")
def get_mask_card_number(card_number: str) -> str:
    """Функция скрывающая полный номер карты"""

    if len(card_number) == 16 and card_number.isdigit():
        return f'{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}'
    return 'Неправильный номер карты'

def test_ok_number():
    assert get_mask_card_number("1234123412341234") == "1234 12** **** 1234"


def test_error():
    assert get_mask_card_number("12345") == "Неправильный номер карты"
