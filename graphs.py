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

#DSU
#Iterative Find()
def find(u):
    while True:
        if parent[u] == u:
            x = u
            break

        else:
            u = parent[u]

    return x

#Iterative Recursive
def find(u):
    if parent[u] == u:
        return u
    parent[u] = find(parent[u])
    return parent[u]

#Union
def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return

    else:
        parent[a] = b
        return

#Dijkstra's algorithm
##Inefficient implementation
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