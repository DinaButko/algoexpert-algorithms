def transposeMatrix(matrix):
    # Create an empty matrix to store the transposed result
    newMatrix = []

    # Loop through each column of the original matrix
    for column in range(len(matrix[0])):  # len(matrix[0]) gives number of columns

        newRow = []  # A new row for the transposed matrix

        # Loop through each row of the original matrix
        for row in range(len(matrix)):  # len(matrix) gives number of rows
            newRow.append(matrix[row][column])  # Add the element to the new row

        newMatrix.append(newRow)  # Append the new row to the transposed matrix

    return newMatrix