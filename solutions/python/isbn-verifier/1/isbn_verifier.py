def is_valid(isbn):
    isbn_cleaned = isbn.replace("-", "")
    isbn_array = list(isbn_cleaned)
    if len(isbn_array) == 10:
        if isbn_array[-1] == "X":
            isbn_array[-1] = "10"
        count = 10
        sum = 0
        for digit in isbn_array:
            try:
                digit_int = int(digit)
                sum += int(digit_int) * count
                count-=1
            except:
                return False
        result = sum % 11
        return result == 0
    else:
        return False
