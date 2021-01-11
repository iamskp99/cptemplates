#Checks if a string is palindrome or not
def ispal(s):
    i = 0
    j = len(s)-1
    f = 1
    while i < j:
        if s[i] != s[j]:
            f = 0
            break

        i += 1
        j -= 1

    return  f