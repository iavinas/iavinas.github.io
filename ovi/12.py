# BFS

MAX = 100

c = [[0]*MAX for _ in range(MAX)]
visited = [0]*MAX
queue = [0]*MAX

def BFS(v):
    front = 0
    rear = -1

    visited[v] = 1
    queue[rear + 1] = v
    rear += 1

    while front <= rear:
        v = queue[front]
        front += 1

        print(f"{v} ", end="")

        for i in range(1, n+1):
            if c[v][i] == 1 and visited[i] == 0:
                queue[rear + 1] = i
                rear += 1
                visited[i] = 1

if __name__ == "__main__":
    print("Enter the number of vertices in the graph: ")
    n = int(input())

    print("Enter the cost matrix of the graph: ")
    for i in range(1, n+1):
        c[i] = [0] + list(map(int, input().split()))

    for i in range(1, n+1):
        visited[i] = 0

    print("Enter the starting vertex: ")
    v = int(input())

    print("BFS traversal of the graph is: ", end="")
    BFS(v)



# Enter the number of vertices in the graph: 
# 6
# 0 1 1 0 0 0
# 1 0 0 1 1 0
# 1 0 0 0 0 1
# 0 1 0 0 1 0
# 0 1 0 1 0 0
# 0 0 1 0 0 0
# Enter the starting vertex: 
# 1
# BFS traversal of the graph is: 1 2 3 4 5 6