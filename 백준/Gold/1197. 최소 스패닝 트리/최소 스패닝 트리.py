import sys
input = sys.stdin.readline

V, E = map(int, input().split())

edges = [] # 간선
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2]) # 비용이 적은 것부터 정렬

# 부모 정점을 저장할 배열(1부터 시작)
parent = [i for i in range(V+1)]

def get_parent(x): # 재귀적으로 찾아감
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b: # 작은 쪽이 부모가 된다.
        parent[b] = a
    else:
        parent[a] = b        

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

total = 0
for a, b, cost in edges:
    # 같은 부모를 가지고 있지 않을 때만
    if not same_parent(a, b):
        union_parent(a, b)
        total += cost
print(total)