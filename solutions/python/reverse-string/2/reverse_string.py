def reverse(text):
    result = ""
    for t in range(len(text)-1, -1, -1):
        result += text[t]
    return result
        
