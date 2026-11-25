def is_armstrong_number(number):
    if number < 0 :
        return False
    num_str = str(number)
    power = len(num_str)

    total = 0
    for num in num_str:
        total += int(num) ** power

    if total == number:
        return True
    return False
