def is_pangram(sentence):
    sentence_lower = "".join([char for char in sentence.lower() if char.isalpha()])
    tracker = []
    for char in sentence_lower:
        if char not in tracker:
            tracker.append(char)
    if len(tracker) == 26:
        return True
    return False
        
