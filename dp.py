#Kadane's algo
def max_sum(a):
    maxnow = 0
    maximum = 0
    for i in range(len(a)):
        maxnow += a[i]
        if maxnow < a[i]:
            maxnow = a[i]

        maximum = max(maxnow, maximum)

    return maximum
