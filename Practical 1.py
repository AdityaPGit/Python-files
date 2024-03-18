graph={'A':['B','C','D'],'B':['A','E'],'C':['A','D','E'],'D':['A','C'],'E':['B','C']}
visited=set()
def dfs (visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,'A')
