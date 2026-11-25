def rotate(text, key):
    """
    omg -> trl
    
    """
    output = ""
    for t in text:
        if not t.isalpha():
            output += t
            continue

        ch = t.lower()
        transformed = chr(((ord(ch) - ord('a') + key) % 26) + ord('a'))
        if t.isupper():
            output += transformed.upper()
        else:
            output += transformed
    return output 
