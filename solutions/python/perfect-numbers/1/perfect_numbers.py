def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    factors = find_factors(number)
    sum = 0
    for f in factors:
        sum += f
    if sum == number:
        return "perfect"
    elif sum < number:
        return "deficient"
    elif sum > number:
        return "abundant"
    
def find_factors(number):
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    return factors
