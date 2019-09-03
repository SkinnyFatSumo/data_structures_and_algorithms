# leetcode 396 (rotate-function)

def rotateArrayForMaxValue(A):
    len_A = len(A)
    sum_A = products_sum = 0

    for index, value in enumerate(A):
        sum_A += value
        products_sum += index * value
    max_sum = products_sum

    for biggest in range(len_A-1, 0, -1):
        products_sum += sum_A - (len_A * A[biggest])
        max_sum = max(products_sum, max_sum)
        print(products_sum)



