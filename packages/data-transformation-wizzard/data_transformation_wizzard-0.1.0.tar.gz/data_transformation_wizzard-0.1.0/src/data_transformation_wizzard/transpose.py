def transpose2d(input_matrix: list[list[float]]) -> list[list[float]]:
    """
    Transpose a 2D matrix.

    Args:
    input_matrix (List[List[float]]): The input 2D matrix.

    Returns:
    List[List[float]]: The transposed 2D matrix.

    Raises:
    TypeError: If input_array is not a list of lists of numbers.
    ValueError: If input_array does not contain only numbers or if all inner lists do not have the same length.
    """
    # Check if input is a list of lists
    if not all(isinstance(row, list) for row in input_matrix):
        raise TypeError("Input must be a list of lists")
    # Check if all elements of the list are numbers
    if not all(
        all(isinstance(num, (int, float)) for num in row) for row in input_matrix
    ):
        raise ValueError("All elements of the input list must be numbers")
    # Check if all inner lists have the same length
    if not all(len(row) == len(input_matrix[0]) for row in input_matrix):
        raise ValueError("All inner lists must have the same length")
    # Transpose the 2D matrix
    return [list(row) for row in zip(*input_matrix)]


# Test the function
if __name__ == "__main__":
    rows = int(input("Enter the number of rows in the matrix: "))
    cols = int(input("Enter the number of columns in the matrix: "))
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(
                float(input(f"Enter element at position ({i+1}, {j+1}): "))
            )
    print("Original Matrix:")
    for row in matrix:
        print(row)
    print("\nTransposed Matrix:")
    for row in transpose2d(matrix):
        print(row)
