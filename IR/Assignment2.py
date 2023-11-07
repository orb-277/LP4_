# import numpy as np

# # Define the adjacency matrix of the graph
# adjacency_matrix = np.array([
#     [0, 1, 1, 0],
#     [0, 0, 1, 0],
#     [1, 0, 0, 1],
#     [0, 0, 1, 0]
# ], dtype=float)

# out_degree = np.sum(adjacency_matrix, axis=1)


# for i in range (out_degree.shape[0]):
#     pr = 0
#     for j in range(out_degree.shape[0]):
#         if adjacency_matrix[j][i] == 1:
#             pr = pr + (1/out_degree.shape[0])/out_degree[j]
#     print(pr)


import numpy as np

def pagerank(M, num_iterations: int = 100, d: float = 0.85):
    N = M.shape[1]
    v = np.ones(N) / N
    M_hat = (d * M + (1 - d) / N)
    for i in range(num_iterations):
        v = M_hat @ v
    return v

M = np.array([[0, 0, 0, 0, 1],
              [0.5, 0, 0, 0, 0],
              [0.5, 0, 0, 0, 0],
              [0, 1, 0.5, 0, 0],
              [0, 0, 0.5, 1, 0]])
v = pagerank(M, 100, 0.85)
print(v)


            



