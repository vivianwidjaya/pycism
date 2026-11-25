def response(hey_bob):
    hey_bob_stripped = hey_bob.strip()
    is_capitalised = hey_bob_stripped.isupper()
    is_question = hey_bob_stripped.endswith("?")

    if is_question and not is_capitalised:
        return "Sure."
    if is_capitalised and not is_question:
        return "Whoa, chill out!"
    if is_capitalised and is_question:
        return "Calm down, I know what I'm doing!"
    if hey_bob_stripped == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."