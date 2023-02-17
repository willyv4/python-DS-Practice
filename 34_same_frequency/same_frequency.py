def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    return sorted(str(num1)) == sorted(str(num2))

    # num1 = str(num1)
    # num2 = str(num2)

    # lst1 = [int(x) for x in num1]
    # lst2 = [int(x) for x in num2]

    # lst1.sort()
    # lst2.sort()

    # return True if lst1 == lst2 else False


print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
