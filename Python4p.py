# INF = 1000000000
# def floyd_warshall(vertex, adjacency_matrix):
#  # calculating all pair shortest path
#     for k in range(0, vertex):
#         for i in range(0, vertex):
#             for j in range(0, vertex):
#                 adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])
#     print("o/d", end='')
#     for i in range(0, vertex):
#         print("\t{:d}".format(i+1), end='')
#     print()
#     for i in range(0, vertex):
#         print("{:d}".format(i+1), end='')
#         for j in range(0,vertex):
#             print("\t{:d}".format(adjacency_matrix[i][j]), end='')
#         print()
# adjacency_matrix = [
#      [ 0, 5, INF, 10],
#      [ INF, 0, 3, INF],
#      [ INF, INF, 0, 1],
#      [INF, INF, INF, 0]
#      ]
# floyd_warshall(4, adjacency_matrix);

INF = 1000000000


def warshell(vertex, adjmatrix):
    for k in range(vertex):
        for i in range(vertex):
            for j in range(vertex):
                adjmatrix[i][j] = min(adjmatrix[i][j], adjmatrix[i][k] + adjmatrix[k][j])
    print('o/d', end='')
    for i in range(vertex):
        print("\t{:d}".format(i + 1), end='')
    print()
    for i in range(vertex):
        print('{:d}'.format(i + 1), end='')
        for j in range(vertex):
            print("\t{:d}".format(adjmatrix[i][j]), end='')
        print()


adjacency_matrix = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
warshell(4, adjacency_matrix)
