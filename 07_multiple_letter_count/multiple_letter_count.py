def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    my_dict = {}

    for letters in phrase:
        cnt = phrase.count(letters)
        my_dict.update({letters: cnt})
    return my_dict


print(multiple_letter_count("Yay"))
print(multiple_letter_count("yay"))
