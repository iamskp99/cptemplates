#BFS (Shortest path and Search)
from collections import deque
def bfs(start,graph):
    explored = set()
    queue = deque([start])
    levels = {}
    levels[start]= 0
    visited = {start}
    while queue:
        node = queue.popleft()
        explored.add(node)
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                levels[neighbour]= levels[node]+1

    return levels

#Recursion support template
import sys
input = sys.stdin.readline
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


@bootstrap
#(Function Goes Here.Replace every return statement with yeild and before every call add yeild.)

#DFS (Recursive)
def dfs(x,visited,graph):
    if x not in visited:
        visited.add(x)
        for i in graph[x]:
            if i not in visited:
                dfs(i,visited,graph)

    return

#DFS (Iterative)
def dfs(x, visited, graph):
    stack = [x]
    while len(stack) > 0:
        node = stack.pop()
        visited.add(node)
        if node not in graph:
            continue

        for i in graph[node]:
            if i not in visited:
                stack.append(i)

    return

#Dijkstra's algorithm
##Inefficient implementation O(V**2)
def getmin(s):
    e = 10**18
    x = -1
    for i in s:
        if i[0] < e:
            e = i[0]
            x = i

    return x

def dijkstra(v):
    s.add((0,v))
    dist[v] = 0
    while len(s) != 0:
        e = getmin(s)
        u = e[1]
        s.remove(e)
        for i in graph[u]:
            v = i
            w = price[(u,v)]
            if dist[v] > dist[u]+w:
                if dist[v] != 10**18:
                    s.remove((dist[v],v))

                dist[v] = dist[u]+w
                s.add((dist[v],v))

    return

# Connected Components
from collections import deque

def connectedComponent(start,graph,n):
    explored = set()
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        explored.add(node)
        if node not in graph:
            continue

        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

    if len(explored) == n:
        return True

    return False
<<<<<<< HEAD

# Prim's

def prim(start,graph,cost,n):
    key = [10**18]*(n+1)
    mst = [0]*(n+1)
    parent = [-1]*(n+1)
    key[start] = 0
    h = [(0,start)]
    heapq.heapify(h)
    while len(h) > 0:
        x = heapq.heappop(h)
        mst[x[1]] = 1
        for j in graph[x[1]]:
            if mst[j] == 0:
                if (x[1],j) in cost:
                    price = cost[(x[1],j)]

                else:
                    price = cost[(j,x[1])]

                if price < key[j]:
                    parent[j] = x[1]
                    heapq.heappush(h,(price,j))
                    key[j] = price

    return sum(key[1:])

# Kruskal's

import heapq
import sys
input = sys.stdin.readline

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

def kruskal(h,n):
    mst = [0]*(n+1)
    parent = []
    rank = []
    for i in range(n+1):
        parent.append(i)
        rank.append(0)

    ans = 0
    sg = Union(parent,rank)
    while len(h) > 0:
        x = heapq.heappop(h)
        e1 = x[1]
        e2 = x[2]
        if sg.findp(e1) != sg.findp(e2):
            sg.union(e1,e2)
            ans += x[0]

    return ans


#Floyd Warshall

INF = 10**18
# Algorithm
# G is the graph in an adjacency matrix and nV is the no. of nodes

def floyd(G,nV):
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))
    # Adding vertices individually
    for r in range(nV):
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])

    return dist
=======
>>>>>>> c32eb9a92e937cc5e23ca34ee13c39c787e2017a
