. This week's exercise is to write a function that performs a matrix transposition. Matrix 
transposition means swapping the rows and columns of a matrix. For example, if you 
have a 2x3 matrix: 
1 2 3 
 
4 5 6 
 
The transposed matrix would be a 3x2 matrix: 
 
1 4 
2 5 
3 6

def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)] 
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = transpose_matrix(matrix)
for row in result:
    print(*row)
