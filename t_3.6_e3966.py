def binary_search(arr, el):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] < el:
            l = mid + 1
        elif arr[mid] > el:
            r = mid - 1
        elif arr[mid] == el:
                return True
    return False


with open("input") as file:
    temp_1 = file.readline()
    arr = [int(el) for el in file.readline().split()]
    temp_2 = file.readline()
    needed_species = [int(el) for el in file.readline().split()]
    for el in needed_species:
        if binary_search(arr, el):
            print("YES")
        else:
            print("NO")