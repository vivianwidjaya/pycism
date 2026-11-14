def ohm_reading_processor(value):
    if value == 0:
        return f"{value} ohms"
    elif (value % 1000000000 == 0):
        return f"{value//1000000000} gigaohms"
    elif (value % 1000000 == 0):
        return f"{value//1000000} megaohms"
    elif (value % 1000 == 0):
        return f"{value//1000} kiloohms"
    else:
        return f"{value} ohms"

def ohm_unit_calculator(int_value):
    return 10**int_value
        
def label(colors):
    band_value = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    ohm_value = []
    for color in colors:
        if color in band_value:
            ohm_value.append(band_value[color])

    ohm_unit = ohm_unit_calculator(ohm_value[2])
               
    ohm_reading = (ohm_value[0]*10 + ohm_value[1]) * ohm_unit

    ohm_output = ohm_reading_processor(ohm_reading)

    return ohm_output
