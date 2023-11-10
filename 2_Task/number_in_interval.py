
def number_in_interval(number):
    if not isinstance(number, (int, float)):
        raise ValueError('Введите Число!')

    if not 25 <= number <= 100:
        return False
    else:
        return True


print(number_in_interval(101))











