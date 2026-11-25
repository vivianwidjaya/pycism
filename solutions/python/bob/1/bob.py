def response(hey_bob):
    hey_bob_stripped = hey_bob.strip()
    is_capitalised = hey_bob_stripped.isupper()
    is_question = hey_bob_stripped.endswith("?")

    if is_question and not is_capitalised:
        return "Sure."
    elif is_capitalised and not is_question:
        return "Whoa, chill out!"
    elif is_capitalised and is_question:
        return "Calm down, I know what I'm doing!"
    elif hey_bob_stripped == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."