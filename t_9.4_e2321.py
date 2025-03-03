def sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    _sort(array, 0, len(array) - 1)


def _sort(array, a, b):
    if a >= b:
        return
    pivot = array[a + (b - a + 1) // 2]
    left = a
    right = b
    while True:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1

        if left >= right:
            break

        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    _sort(array, a, left - 1)
    _sort(array, left, b)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    sort(arr)
    print(*arr)