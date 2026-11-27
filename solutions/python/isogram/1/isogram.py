def is_isogram(phrase):
    phrase_cleaned = "".join([char for char in phrase.lower() if char.isalpha()])
    tracker = []
    for char in phrase_cleaned:
        if char not in tracker:
            tracker.append(char)
    if len(tracker) == len(phrase_cleaned):
        return True
    else:
        return False
