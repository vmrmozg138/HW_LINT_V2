from time import time


def log(filename=None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            '''Декоратор для логирования выполнеия функции- логируется время, а в случае ошибки - наименование ошибки и аргументы функции, вызов с которыми привел к ошибке'''
            time_1 = time()
            try:
                result = func(*args, **kwargs)
                mylog = f"{func.__name__} ok"
            except Exception as e:
                result = e
                mylog = f"{func.__name__} error: {type(e).__name__}. Inputs: {args, kwargs}  "
            finally:
                time_2 = time()
            mylog += f"Время работы {time_2 - time_1} секунд"
            if filename:
                with open(filename, "a") as f:
                    f.write(mylog)
            else:
                print(mylog)
            return result

        return wrapper

    return my_decorator
