def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
        return

    if number == 1:
        return 0
        
    steps_no = 0
    while number > 1:
        if (number%2 == 0):
            number /= 2
            steps_no+=1
        else:
            number = number * 3 + 1
            steps_no+=1
    return steps_no

    
        
        
        
