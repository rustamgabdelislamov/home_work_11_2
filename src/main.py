import time

def log(filename):
    def my_decorator(func):
        def inner(*args, **kwargs):
            time_1 = time.time()
            print(f'Function {func.__name__} started at {time_1}')
            try:
                result = func(*args, **kwargs)

                # Логируем успешное выполнение функции
                log_message = f"{func.__name__} executed successfully. Result: {result}"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(log_message + '\n')
                else:
                    print(log_message)

                return result
            except Exception as e:
                # Получаем входные данные для сообщения об ошибке
                inputs = ', '.join(map(str, args))  # Преобразуем аргументы в строку
                error_message = f"{func.__name__} error: {str(e)}. Inputs: {inputs}"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(error_message + '\n')
                else:
                    print(error_message)

        return inner

    return my_decorator

@log(filename="log.txt")
def get_mask_card_number(card_number: str) -> str:
    """Функция скрывающая полный номер карты"""
    if len(card_number) == 16 and card_number.isdigit():
        return f'{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}'
    else:
        raise ValueError('Неправильный номер карты')  # Генерируем исключение для обработки ошибки

# Примеры использования
print(get_mask_card_number("1234567812345678"))  # Должно вернуть замаскированный номер и записать в лог
print(get_mask_card_number("12345"))              # Должно вызвать исключение и записать в лог
print(get_mask_card_number("12345678123456AB"))   # Должно вызвать исключение и записать в лог
