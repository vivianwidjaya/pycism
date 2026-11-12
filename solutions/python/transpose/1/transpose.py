def transpose(text):
    lines = text.split('\n')
    transposed_text = ""
    for i in range(len(max(lines, key=len))):
        for j in range(len(lines)):
            if i < len(lines[j]):
                transposed_text += lines[j][i]
            elif any(len(line) > i for line in lines[j:]):
                transposed_text += " "
            else:
                transposed_text += ""
        transposed_text += "\n"
    return transposed_text[:-1]