def solve(arr, a, b):
    counter = 0
    for el in arr:
        if a < el < b:
            counter += 1
    return counter

with open("input.txt") as file:
    while file.readline():
        arr = [int(el) for el in file.readline().split()]
        a, b = [int(el) for el in file.readline().split()]
        print(solve(arr, a, b))