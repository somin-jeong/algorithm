# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
  if graph[x][y] == 0:
    graph[x][y] = 1
    if x < n-1:
      dfs(x+1, y)
    if x > 0:
      dfs(x-1, y)
    if y < m-1:
      dfs(x, y+1)
    if y > 0:
      dfs(x, y-1)
    return True
  return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) is True:
      result += 1

print(result)