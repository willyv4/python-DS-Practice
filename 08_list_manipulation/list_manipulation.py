lst = [1, 2, 3]


def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    command = command.lower()
    location = location.lower()

    if command == "add" and location == "beginning":
        lst.insert(0, value)
        return lst
    if command == "add" and location == "end":
        lst.insert(len(lst), value)
        return lst
    if command == "remove" and location == "end":
        return lst.pop(-1)
    if command == "remove" and location == "beginning":
        return lst.pop(0)
    else:
        return None

    if command not in ('add', 'remove') or location not in ('beginning', 'end'):
        return None

    if command == 'add':
        if location == 'beginning':
            lst.insert(0, value)
        else:
            lst.append(value)
        return lst
    else:
        if location == 'beginning':
            return lst.pop(0)
        else:
            return lst.pop()


print(list_manipulation(lst, 'Add', 'end', "oops"))

print(list_manipulation(lst, 'Add', 'beginning', "oops"))

print(list_manipulation(lst, 'remove', 'end'))

print(list_manipulation(lst, 'remove', 'beginning'))

print(list_manipulation(lst, 'foo', 'end'))

print(list_manipulation(lst, 'add', 'dunno'))
