def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    count = 0
    vowel_frequency = {}
    phrase = phrase.lower()

    for letter in phrase:
        if letter in vowels:
            count += 1
            if letter in vowel_frequency:
                vowel_frequency[letter] += 1
            else:
                vowel_frequency[letter] = 1
    return vowel_frequency


print((vowel_count('HOW ARE YOU? i am great!')))
