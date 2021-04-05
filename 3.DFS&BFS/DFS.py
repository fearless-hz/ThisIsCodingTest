graph=[ #노드 간 연결정보
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9 #방문 여부 저장. 초기에는 전부 FALSE로 설정
def dfs(graph,visited,v):
    visited[v]=True #해당 노드 방문 처리
    print(v,end=' ')
    for i in graph[v]: #해당 노드와 연결된 노드를 재귀적으로 방문
        if not visited[i]: #방문처리 안됐으면 재귀함수 호출해서 방문처리
            dfs(graph,visited,i)

dfs(graph,visited,1)