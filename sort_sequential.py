# Iterative function to find the maximum sum of an increasing subsequence
def MSIS(A):

    # list to store subproblem solutions. `sum[i]` stores the maximum
    # sum of the increasing subsequence that ends with `A[i]`
    sum = [0] * len(A)

    # base case
    sum[0] = A[0]

    # start from the second element in the list
    for i in range(1, len(A)):

        # do for each element in sublist `A[0…i-1]`
        for j in range(i):

            # find increasing subsequence with the maximum sum that ends with
            # `A[j]`, where `A[j]` is less than the current element `A[i]`
            if sum[i] < sum[j] and A[i] > A[j]:
                sum[i] = sum[j]

        # include `A[i]` in MSIS
        sum[i] += A[i]

    # find increasing subsequence with the maximum sum
    return max(sum)


if __name__ == '__main__':

    A = [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]

    print("The maximum sum of the increasing subsequence is", MSIS(A))
