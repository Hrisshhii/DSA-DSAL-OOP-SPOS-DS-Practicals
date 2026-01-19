from collections import deque

def dfs(node,adj,visited):
    visited.add(node)
    print(node,end=" ")
    for neighbor in adj[node]:
        if neighbor not in visited:
            dfs(neighbor,adj,visited)

def bfs(queue,adj,visited):
    if not queue:
        return
    node=queue.popleft()
    print(node,end=" ")
    for neighbor in adj[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    bfs(queue,adj,visited)

def main():
    adj={}
    n=int(input("Enter the number of nodes: "))
    for i in range(n):
        node=int(input(f"Enter node {i}: "))
        neighbors=list(map(int,input("Enter neighbors of {node}: ").split()))
        adj[node]=neighbors
    start=int(input("Enter starting node: "))
    print("\nDFS Traversal: ")
    visited=set()
    dfs(start,adj,visited)

    print("\n\nBFS Traversal")
    visited=set([start])
    q=deque([start])
    bfs(q,adj,visited)

main()