#This function takes list of tuples and sorts the list in reverse with first element of the first tuple as greatest and second
#elemet of the tuple as least.
def strange(l):
    l.sort(reverse=True, key=lambda x:(x[0],-x[1]))
    return

#Activity Selection Problem
def max_acitivity(n, start, end):
    # code here
    l = []
    for i in range(n):
        l.append((start[i], end[i]))

    l.sort(key=lambda x: x[1])
    ans = 1
    i = 0
    j = i + 1
    while i < n and j < n:
        #There can be a greater than equal to sign.
        if l[j][0] > l[i][1]:
            i = j
            j = i + 1
            ans += 1

        else:
            j = j + 1

    return ans

