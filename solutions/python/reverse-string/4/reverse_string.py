def reverse(text):
    return reverse_helper(text, 0, "")

def reverse_helper(text, idx, reverse_text):
    if idx > len(text) - 1:
        return reverse_text
    return reverse_helper(text, idx + 1, text[idx] + reverse_text)

