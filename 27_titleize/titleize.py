def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    word_lst = phrase.split()
    new_list = []

    for word in word_lst:
        word = word.lower()
        new_list.append(word.replace(word[0], word[0].upper()))

    return ' '.join(new_list)


print(titleize('oNLy cAPITALIZe fIRSt'))
