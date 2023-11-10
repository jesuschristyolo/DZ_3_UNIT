
def even_odd_number(number):
    if not isinstance(number, (float, int)):
        raise ValueError("Введите числовое значение")


    if number % 2 == 0:
        return True
    else:
        return False


# print(even_odd_number('y'))









