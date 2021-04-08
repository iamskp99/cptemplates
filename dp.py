#Kadane's algo
def max_sum(a):
    maxnow = a[0]
    maximum = a[0]
    for i in range(1,len(a)):
        maxnow += a[i]
        if maxnow < a[i]:
            maxnow = a[i]

        maximum = max(maxnow, maximum)

    return maximum