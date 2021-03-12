#Check if a number is prime or not in O(n**0.5)
def chkPrime(n):
    flag = 1
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            flag = 0
            break

    return flag

#Returns set prime factors O(n**2)
import math
def primefactors(n):
    l = set()
    while n % 2 == 0:
        l.add(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            l.add(i)
            n = n // i

    if n > 2:
        l.add(n)

    return l

#Returns set prime factors O(nloglogn) (Pre-computation),log n per query
import math as mt
MAXN = 1000000+101
spf = [0 for i in range(MAXN)]

def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i

    for i in range(4, MAXN, 2):
        spf[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(MAXN))):
        if (spf[i] == i):
            for j in range(i * i, MAXN, i):
                if (spf[j] == j):
                    spf[j] = i

def getFactorization(x):
    ret = set()
    while (x != 1):
        ret.add(spf[x])
        x = x // spf[x]

    return ret

sieve()

import math

#Return Divisors O(n**2)
def divisors(n):
    i = 1
    l = []
    while i <= int(n**0.5):
        if (n % i == 0):
            if (n // i == i):
                l.append(i)

            else:
                l.append(n // i)
                l.append(i)

        i = i + 1

    return l

#Factorial with modulo
M = 10**9+7
fact = [0]*1000001
fact[0] = 1
i = 1
while(i < len(fact)):
    x = (fact[i-1]*i)%M
    fact[i] = x
    i = i+1

#Fast modular exponentiation
def power(x,y):
    ans = 1
    while(y>0):
        if(y%2 == 1):
            ans = (ans*x)%M
        y = y //2
        x = (x*x)%M
    return ans%M

#Permutation with modulo
M = (10 ** 9) + 7
def inv(n):
    return power(n, M - 2)


def power(x, y):
    ans = 1
    while (y > 0):
        if (y % 2 == 1):
            ans = (ans * x) % M
        y = y // 2
        x = (x * x) % M

    return ans % M

def per(n, r):
    if r == 0:
        return 1

    else:
        return ((f[n] * inv(f[n - r]) % M)) % M

f = [1]
x = 1
for i in range(1, 10 ** 5 + 3):
    x = (x * i) % M
    f.append(x)

#Combination with modulo
M = (10 ** 9) + 7
def inv(n):
    return power(n, M - 2)

def power(x, y):
    ans = 1
    while (y > 0):
        if (y % 2 == 1):
            ans = (ans * x) % M
        y = y // 2
        x = (x * x) % M

    return ans % M

def com(n, r):
    if r == 0:
        return 1

    else:
        return (((f[n] * inv(f[n - r]) % M)* inv(f[r]))%M) % M

f = [1]
x = 1
for i in range(1, 10 ** 5 + 3):
    x = (x * i) % M
    f.append(x)

#Matrix exponentiation fibonacci
M = 10**9+7
def multiply(m1,m2):
    r = []
    for i in range(len(m1)):
        o = []
        for j in range(len(m1)):
            o.append(0)

        r.append(o)

    for i in range(len(m1)):
        for j in range(len(m2)):
            som = 0
            for k in range(len(m1[i])):
                som = (som+(m1[i][k]*m2[k][j])%M)%M

            r[i][j] = som

    return r

def power(n):
    ans = [[1,0],[0,1]]
    m = [[1,1],[1,0]]
    while(n != 0):
        if n%2 == 1:
            ans = multiply(ans,m)

        m = multiply(m,m)
        n = n//2

    return ans[0][0]

#Ceil check function
def chk(p, a):
    if p % a == 0:
        return 0

    return 1

