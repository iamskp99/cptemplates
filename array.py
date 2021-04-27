class SegmentTree:
    def __init__(self,l,identityVal,combine):
        self.l = [0]+l
        self.n = len(self.l)-1
        self.identityVal = identityVal
        self.st = [identityVal]*(4*self.n)
        # self.lazy = [0]*(4*self.n)
        self.combine = combine
        self.buildTree(1,1,self.n)

    def buildTree(self,si,ss,se):
        if ss == se:
            self.st[si] = self.l[ss]
            return self.st[si]

        mid = (ss+se)//2
        val1 = self.buildTree(2*si,ss,mid)
        val2 = self.buildTree((2*si)+1,mid+1,se)
        self.st[si] = self.combine(val1,val2)
        return self.st[si]

    def queryHelper(self,si,ss,se,qs,qe):
        if qs > se or qe < ss:
            return self.identityVal

        if ss >= qs and se <= qe:
            return self.st[si]

        mid = (ss+se)//2
        l = self.queryHelper(2*si,ss,mid,qs,qe)
        r = self.queryHelper(2*si+1,mid+1,se,qs,qe)
        return self.combine(l,r)

    def pointUpdateHelper(self,si,ss,se,qi):
        if ss == se:
            self.st[si] = self.l[ss]
            return

        mid = (ss+se)//2
        if qi <= mid:
            self.pointUpdateHelper(2*si,ss,mid,qi)

        else:
            self.pointUpdateHelper((2 * si)+1, mid+1, se, qi)

        self.st[si] = self.combine(self.st[2*si],self.st[(2*si)+1])
        return

    def query(self,qs,qe):
        return self.queryHelper(1,1,self.n,qs,qe)

    def pointUpdate(self,val,qi):
        self.l[qi] = val
        return self.pointUpdateHelper(1,1,self.n,qi)

class SegmentTreeLazy:
    def __init__(self,l,identityVal,combine):
        self.l = [identityVal]+l
        self.n = len(self.l)-1
        self.identityVal = identityVal
        self.st = [identityVal]*(4*self.n)
        self.lazy = [0]*(4*self.n)
        self.combine = combine
        self.buildTree(1,1,self.n)

    def buildTree(self,si,ss,se):
        if ss == se:
            self.st[si] = self.l[ss]
            return self.st[si]

        mid = (ss+se)//2
        val1 = self.buildTree(2*si,ss,mid)
        val2 = self.buildTree((2*si)+1,mid+1,se)
        self.st[si] = self.combine(val1,val2)
        return self.st[si]

    def queryHelper(self,si,ss,se,qs,qe):
        if self.lazy[si] != 0:
            dx = self.lazy[si]
            self.lazy[si] = 0
            self.st[si] += (dx*(se-ss+1))
            if ss != se:
                self.lazy[2 * si] += dx
                self.lazy[(2 * si) + 1] += dx


        if qs > se or qe < ss:
            return self.identityVal

        if ss >= qs and se <= qe:
            return self.st[si]

        mid = (ss+se)//2
        l = self.queryHelper(2*si,ss,mid,qs,qe)
        r = self.queryHelper(2*si+1,mid+1,se,qs,qe)
        return self.combine(l,r)

    def rangeUpdateHelper(self,si,ss,se,qs,qe,val):
        if self.lazy[si] != 0:
            dx = self.lazy[si]
            self.lazy[si] = 0
            self.st[si] += (dx * (se - ss + 1))
            if ss != se:
                self.lazy[2 * si] += dx
                self.lazy[(2 * si) + 1] += dx

        if qs > se or qe < ss:
            return

        if ss >= qs and se <= qe:
            dx = (se-ss+1)*val
            self.st[si] += dx
            if ss != se:
                self.lazy[2 * si] += val
                self.lazy[(2 * si) + 1] += val

            return

        mid = (ss + se) // 2
        self.rangeUpdateHelper(2*si,ss,mid,qs,qe,val)
        self.rangeUpdateHelper((2 * si)+1, mid+1, se, qs, qe, val)
        self.st[si] = self.st[2 * si] + self.st[2 * si + 1]
        return

    def pointUpdateHelper(self,si,ss,se,qi):
        if ss == se:
            self.st[si] = self.l[ss]
            return

        mid = (ss+se)//2
        if qi <= mid:
            self.pointUpdateHelper(2*si,ss,mid,qi)

        else:
            self.pointUpdateHelper((2 * si)+1, mid+1, se, qi)

        self.st[si] = self.combine(self.st[2*si],self.st[(2*si)+1])
        return

    def query(self,qs,qe):
        return self.queryHelper(1,1,self.n,qs,qe)

    def pointUpdate(self,val,qi):
        self.l[qi] = val
        return self.pointUpdateHelper(1,1,self.n,qi)

    def rangeUpdate(self,qs,qe,val):
        self.rangeUpdateHelper(1,1,self.n,qs,qe,val)

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

#Prefix Range Sum (GIVES SUM OVER A RANGE)
def makePrefixArray(l):
    prefix = [0]
    for i in l:
        prefix.append(prefix[-1]+i)

    return prefix

def getRangeSum(start,end,parray):
    if start <= 0 or end >= len(parray):
        return -1

    else:
        return parray[end]-parray[start-1]