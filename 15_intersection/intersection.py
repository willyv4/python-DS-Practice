def intersection(l1, l2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    new_lst = []
    for nums1 in l1:
        for nums2 in l2:
            if nums1 == nums2:
                new_lst.append(nums1)

    return new_lst


print(intersection([1, 2, 3], [2, 3, 4]))
print(intersection([1, 2, 3], [1, 2, 3, 4]))
print(intersection([1, 2, 3], [3, 4]))
print(intersection([1, 2, 3], [4, 5, 6]))
