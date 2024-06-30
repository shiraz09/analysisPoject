"""
Shiraz Nagaoker 208324194
Moran Avraham 211778634
Gabriela brailovsky 318804291
"""


"""
    Calculate the inverse of a square matrix using Gaussian elimination.

    Args:
    matrix (list of lists): The input square matrix to be inverted.

    Returns:
    list of lists: The inverse of the input matrix.

    Raises:
    ValueError: If the matrix is singular and cannot be inverted.
    """
def inverse_matrix(matrix):
    n = len(matrix)
    identity_matrix = [[float(i == j) for i in range(n)] for j in range(n)]
    augmented_matrix = [matrix[i] + identity_matrix[i] for i in range(n)]

    for j in range(n):
        # Make the diagonal contain all ones
        diag_element = augmented_matrix[j][j]
        if diag_element == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        for k in range(2 * n):
            augmented_matrix[j][k] /= diag_element

        for i in range(n):
            if i != j:
                pivot1 = (-augmented_matrix[i][j]) / (augmented_matrix[j][j])
                for k in range(2 * n):
                    augmented_matrix[i][k] += pivot1 * augmented_matrix[j][k]

    inverse_matrix = [row[n:] for row in augmented_matrix]
    return inverse_matrix

"""
    Calculate the infinity norm (maximum absolute row sum) of a matrix.

    Args:
    matrix (list of lists): The input matrix.

    Returns:
    float: The infinity norm of the matrix.
    """
def infinity_norm(matrix):
    norm = 0
    for row in matrix:
        row_sum = sum(abs(element) for element in row)
        norm = max(norm, row_sum)
    return norm

"""
    Print a matrix in a readable format.

    Args:
    matrix (list of lists): The matrix to be printed.
    """
def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    matrix_A = [
        [1, -1, -2],
        [2, -3, -5],
        [-1, 3, 5],
    ]

    try:
        inv_matrix_A = inverse_matrix(matrix_A)
        norm_inf_A = infinity_norm(matrix_A)
        norm_inf_inv_A = infinity_norm(inv_matrix_A)

        print("Inverse matrix:")
        print_matrix(inv_matrix_A)
        print(f"\n")

        norm_inf_value_A = infinity_norm(matrix_A)
        print(f"||A||∞, is {norm_inf_value_A}")

        norm_inf_value_inv_A = infinity_norm(inv_matrix_A)
        print(f"||A^-1||∞, is {norm_inf_value_inv_A}")

        condition_number = norm_inf_A * norm_inf_inv_A
        print(f"COND = ||A||∞ * ||A^-1||∞ is {condition_number}")

    except ValueError as e:
        print(e)