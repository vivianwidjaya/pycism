def color_code(color):
    match color:
        case "black":
            return 0
        case "brown":
            return 1
        case "red":
            return 2
        case "orange":
            return 3
        case "yellow":
            return 4
        case "green":
            return 5
        case "blue":
            return 6
        case "violet":
            return 7
        case "grey":
            return 8
        case "white":
            return 9
            
def value(colors):
    first_digit = color_code(colors[0])
    second_digit = color_code(colors[1])

    return first_digit * 10 + second_digit