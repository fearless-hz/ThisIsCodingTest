n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m : #x,y 값이 범위를 벗어나면 바로 종료
        return False
    if graph[x][y]==0 : #해당 노드값이 방문처리 X
        graph[x][y]=1 #해당 노드 방문처리
        dfs(x-1,y) #해당노드 기준 상하좌우 방문처리 수행(return 값 없음!)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True #전부 수행 후 True 반환
    return False #방문처리 되어있을 경우 False 반환

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True: #해당 노드(시작점 기준)가 True 반환시
            result+=1 #return 값 증가

print(result)