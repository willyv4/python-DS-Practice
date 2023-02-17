def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # new_lst = []

    # for item in lst:
    #     if isinstance(item, list):
    #         new_lst.append(item)
    #     else:
    #         return False

    # if new_lst != []:
    #     return True

    return all(isinstance(item, list) for item in lst)


print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))
print(list_check([[1], [2, 3]]))
print(list_check(["nope", "nope", [1], [1]]))
