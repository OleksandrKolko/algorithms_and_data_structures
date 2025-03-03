def sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    _sort(array, 0, len(array) - 1)

def _sort(array: list[list], a, b):
    if a == b:
        return

    m = a + (b - a) // 2
    _sort(array, a, m)
    _sort(array, m + 1, b)

    left = array[a: m + 1]
    i = 0
    j = m + 1
    k = a
    while i < len(left) and j <= b:
        if left[i][0] == array[j][0]:
            array[k] = left[i]
            k += 1
            array[k] = array[j]
            i += 1
            j += 1
        elif left[i][0] < array[j][0]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = array[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

if __name__ == "__main__":
    with open("input") as file:
        n = int(file.readline())
        array = []
        for _ in range(n):
            array.append([int(x) for x in file.readline().split()])

    sort(array)
    for el in array:
        print(*el)