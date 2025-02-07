def prefix_sums(X, R):
    prefix = [0] * (R + 1)
    for i in range(R):
        prefix[i + 1] = prefix[i] + X[i]
    return prefix

def medians(X, R, k):
    for i in range(R - k + 1):
        median_index = (i + i + k - 1) // 2
        first_index = i
        last_index = i + k
        median = X[median_index]
        print(X[first_index: last_index], "median =", median)
        yield median, first_index, last_index, median_index

def can_transport(X, R, B, k, prefix):
    for median, first_index, last_index, median_index in medians(X, R, k):
        left_cost = median * (median_index - first_index) - (prefix[median_index] - prefix[first_index])
        print("left cost: ",left_cost)
        right_cost = (prefix[last_index] - prefix[median_index + 1]) - median * (last_index - median_index - 1)
        print("right cost: ",right_cost)
        price = left_cost + right_cost
        print("Total price for median: ",price)
        if price <= B:
            print("Can transport")
            return True
    print("Can not transport")
    return False

def max_trucks(R, L, B, X):
    prefix = prefix_sums(X, R)
    l = 0
    r = R
    while l < r:
        mid = (l + r + 1) // 2
        if can_transport(X, R, B, mid, prefix):
            l = mid
        else:
            r = mid - 1
    return l

if __name__ == '__main__':
    R, L, B = map(int, input().split())
    X = list(map(int, (input().strip() for _ in range(R))))
    print("Result: ", max_trucks(R, L, B, X))