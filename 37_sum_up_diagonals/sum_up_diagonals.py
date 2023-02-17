m1 = [
    [1,   2],
    [30, 40],
]


m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    length = len(matrix)

    count = 0
    for i in range(length):
        print(matrix[i][i])
        print(matrix[i][-1 + i])
        count += matrix[i][i]
        count += matrix[i][-1 + i]

    if length % 2 == 1:
        middle = matrix[length // 2][length // 2]
        count -= matrix[length // 2][length // 2]
        count += middle

    return count


print(sum_up_diagonals(m1))
print(sum_up_diagonals(m2))
