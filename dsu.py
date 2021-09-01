class Union():
    def __init__(self,parent,rank):
        self.parent = parent
        self.rank = rank

    def union(self, a, b):
        e1 = self.findp(a)
        e2 = self.findp(b)
        if e1 == e2:
            return e1

        if self.rank[e1] < self.rank[e2]:
            self.parent[e1] = self.parent[e2]
            return e2

        elif self.rank[e1] > self.rank[e2]:
            self.parent[e2] = self.parent[e1]
            return e1

        else:
            self.parent[e1] = self.parent[e2]
            self.rank[e1] += 1
            return e2

    def findp(self, a):
        if self.parent[a] == a:
            return a

        self.parent[a] = self.findp(self.parent[a])
        return self.parent[a]