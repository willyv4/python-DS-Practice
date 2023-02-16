def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    backwards_sentence = phrase[::-1].lower().replace(" ", "")
    regular_sentence = phrase.lower().replace(" ", "")

    return True if backwards_sentence == regular_sentence else False


print(is_palindrome('tacocat'))
print(is_palindrome('noon'))
print(is_palindrome('robert'))
print(is_palindrome('Noon'))
print(is_palindrome('taco cat'))
