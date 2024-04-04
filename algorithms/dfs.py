
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for n in graph[start] - visited:
        dfs(graph, n, visited)

    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}
print(dfs(graph, '0'))
