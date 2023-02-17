def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.

        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}

    If there are fewer values than keys, remaining keys should have value
    of None:

        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}

    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
    """

    new_dict = {}
    dif = abs(len(keys) - len(values))

    for k_inx, key in enumerate(keys):
        if k_inx < len(values):
            new_dict[key] = values[k_inx]
        elif len(keys) > len(values):
            new_dict[key] = None

    return new_dict


print(two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]))
print(two_list_dictionary(['a', 'b', 'c', 'd', 'e'], [1, 2, 3]))
print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))
