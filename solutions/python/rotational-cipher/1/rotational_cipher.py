def rotate(text, key):
    """
    omg -> trl
    
    """
    output = ""
    for t in text:
        if t.isupper():
            output += chr(((ord(t) - ord('A') + key) % 26) + ord('A'))
        elif t.islower():
            output += chr(((ord(t) - ord('a') + key) % 26) + ord('a'))
        else:
            output += t
    return output 
