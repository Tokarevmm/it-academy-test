def transpose_matrix(matrix):

    rows, cols = len(matrix), len(matrix[0])

    transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    print("Исходная матрица:")
    for row in matrix:
        print(row)
    print(f"Размер матрицы: {rows} x {cols}")

    print("\nТранспонированная матрица:")
    for row in transpose:
        print(row)
    print(f"Размер матрицы: {cols} x {rows}")


M = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
transpose_matrix(M)