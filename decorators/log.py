import time


def log(filename=""):
    def my_decorator(func):
        def inner(*args, **kwargs):
            time_1 = time.time()
            print(f'Function {func.__name__} started at {time_1}')
            result = func(*args, **kwargs)
            if "*" in result:
                log_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(log_message + '\n')
                    print(log_message)
                else:
                    print(log_message)
                return result
            else:
                inputs = ", ".join(map(str, args))
                error_message = f"{func.__name__} error: {result}. Inputs: {inputs}"

                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(error_message + '\n')
                    print(error_message)
                else:
                    print(error_message)
                return result
        return inner

    return my_decorator
