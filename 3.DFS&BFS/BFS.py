from collections import deque
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

visited = [False]*9

def bfs(graph,visited,start):
    queue = deque([start]) #큐 구현 위해 deque 라이브러리 사용

    visited[start]=True #현재 노드 방문처리
    while queue : #큐가 빌 때까지 반복
        #print(queue)
        v = queue.popleft() #큐에서 원소 뽑아 출력
        print(v,end=' ')

        for i in graph[v]:
            if not visited[i]: #방문처리 안된 노드일 경우
                queue.append(i) #큐에 노드 삽입
                visited[i]=True #해당노드 방문처리
bfs(graph,visited,1)