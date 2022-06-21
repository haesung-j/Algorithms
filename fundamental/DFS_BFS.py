
'''
DFS: Depth-First Search
- 깊이 우선 탐색
- stack 자료구조 or recursive function
<동작 과정>
1. 탐색 시작 노드를 스택에 삽입 후 방문 처리
2. 스택 최상단 노드에 방문하지 않은 인접 노드가 하나라도 있을 시, 그 노드를 스택에 넣고 방문 처리
  - 만약 인접 노드를 모두 방문했다면 스택에서 최상단 노드를 꺼냄
3. 더 이상 2번을 수행할 수 없을 때까지 반복
'''
graph = [
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

visited = [False] * 9

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited)
            
dfs(graph, 1, visited)

'''
BFS: Breadth-First Search
- 너비 우선 탐색
- queue 자료구조
- 특정 조건에서 최단 경로를 찾는 경우 자주 사용됨
<동작 과정>
1. 탐색 시작 노드를 큐에 삽입 후 방문 처리
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
3. 더 이상 2번 과정을 수행할 수 없을 때가지 반복
'''

graph = [
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


visited = [False] * 9

from collections import deque
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

bfs(graph, 1, visited)


'''
[문제] 음료수 얼려 먹기
- N x M 크기 얼음틀
- 구멍이 뚫린 부분 0, 칸막이 존재 부분 1
- 얼음 틀 모양이 주어졌을 때, 생성되는 총 아이스크림의 개수를 구하는 프로그램 작성

<IDEA>
DFS 혹은 BFS로 해결
1. 첫 노드 방문 처리 후 상,하,좌,우를 살펴보고 값이 0이면서 아직 방문하지 않았으면 방문 처리
2. 방문한 지점에서 다시 상,하,좌,우를 살펴보고 방문 반복
3. 모든 노드에 대해 1-2 과정 수행하며 방문하지 않은 지점의 수를 카운트
'''

graph = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]
    
## DFS로 해결하기
def dfs(x, y):
    # 주어진 범위 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1
        
        # 상하좌우에 대해 재귀적 호출하며 dfs
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

n, m = 4, 5
graph = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
            
print(result)

## BFS로 해결하기
from collections import deque

def bfs(x,y):
    move = [(1,0), (-1,0), (0,1), (0,-1)]
    queue = deque([(x,y)])
    cnt = 0
    
    while queue:
        cx, cy = queue.popleft()
        # 방문 처리
        if graph[cx][cy] == 0:
            graph[cx][cy] = 1
            cnt = 1
            
        # 가능한 인접노드 탐색 (4-방향) 및 모두 큐에 추가
        for mov in move:
            nx = cx + mov[0]
            ny = cy + mov[1]
            
            if nx < 0 or ny <0 or nx >= n or ny >= m:
                continue
                
            if graph[nx][ny] == 0:
                queue.append((nx,ny))

    return cnt

n, m = 4, 5
graph = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

res = 0
for i in range(n):
    for j in range(m):
        if bfs(i,j) == 1:
            res += 1
            
print(res)


'''
[문제] 미로 탈출
- N x M 직사각형 형태의 미로
- (1,1)에서 시작해 출구인 (N,M)까지 한 번에 한 칸씩 이동
- 괴물의 위치는 0으로, 괴물이 없는 부분은 1로 표시
- 탈출하기 위해 움직여야 하는 최소 칸의 개수

ex)
5 6
101010
111111
000001
111111
111111

=> 10
'''
n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

from collections import deque

# 특정 노드를 큐에 삽입하고 방문처리
# 큐에서 노드를 꺼낸 뒤에 인접 노드를 모두 큐에 삽입하고 방문 처리
# 인접 노드를 모두 방문할 때까지 반복
x,y = 0,0
queue = deque([(x,y)])

move = [(-1,0), (1,0), (0,-1), (0,1)]
while queue:
    x,y = queue.popleft()

    for mov in move:
        nx = x + mov[0]
        ny = y + mov[1]
        if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] != 1:
            continue
        else:
            graph[nx][ny] = graph[x][y]+ 1
            queue.append((nx,ny))

        
print(graph[n-1][m-1])
