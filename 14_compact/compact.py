def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    to_remove = [False, None, 0, "", (), [], {}]

    for item in to_remove:
        while item in lst:
            lst.remove(item)
    return lst


print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
