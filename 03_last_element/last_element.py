def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> last_element([1, 2, 3])
        3

        >>> last_element([]) is None
        True
    """
    # num_list = len(lst)

    # if num_list == 0:
    #     return None
    # else:
    #     return lst[num_list - 1]

    return lst[-1] if lst else None


print(last_element([1, 4, 5]))
