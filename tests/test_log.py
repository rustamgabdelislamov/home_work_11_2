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


def test_ok_number_(capsys):
    # Вызов функции с корректным номером карты
    result = get_mask_card_number("1234123412341234")

    # Проверка результата
    assert result == "1234 12** **** 1234"

    # Проверка вывода в лог
    captured = capsys.readouterr()
    assert "get_mask_card_number ok" in captured.out


def test_error_(capsys):
    # Вызов функции с некорректным номером карты
    result = get_mask_card_number("12345")

    # Проверка результата
    assert result == "Неправильный номер карты"

    # Проверка вывода в лог
    captured = capsys.readouterr()
    assert "get_mask_card_number error: Неправильный номер карты. Inputs: 12345" in captured.out
