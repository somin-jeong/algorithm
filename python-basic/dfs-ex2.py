from collections import deque

# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))


def bfs(x, y):
  queue = deque([[x,y]])
  # 큐가 빌 때까지 반복
  while queue:
    v = queue.popleft()
    # 현재 위치에서 네 방향으로의 위치 확인
    if v[1] > 0: # 미로찾기 공간 벗어났는지 확인
      if graph[v[0]][v[1]-1] == 1:  # 벽이 아니고, 해당 노드를 처음 방문하는 경우에만 최단거리 기록
        queue.append([v[0], v[1]-1])
        graph[v[0]][v[1]-1] = graph[v[0]][v[1]] + 1
    if v[0] < n-1:
      if graph[v[0]+1][v[1]] == 1:
        queue.append([v[0]+1,v[1]])
        graph[v[0]+1][v[1]] = graph[v[0]][v[1]] + 1
    if v[1] < m-1:
      if graph[v[0]][v[1]+1] == 1:
        queue.append([v[0], v[1]+1])  
        graph[v[0]][v[1]+1] = graph[v[0]][v[1]] + 1
    if v[0] > 0:
      if graph[v[0]-1][v[1]] == 1:
        queue.append([v[0]-1, v[1]])
        graph[v[0]-1][v[1]] = graph[v[0]][v[1]] + 1

  # 가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n-1][m-1]

print(bfs(0,0))