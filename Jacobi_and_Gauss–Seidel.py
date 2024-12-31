# פונקציה לבדיקה אם המטריצה היא בעלת אלכסון דומיננטי
def is_diagonally_dominant(matrix):
    n = len(matrix)
    for i in range(n):
        row_sum = sum(abs(matrix[i][j]) for j in range(n) if j != i)
        if abs(matrix[i][i]) <= row_sum:
            return False
    return True


# פונקציה לשינוי שורות כדי לנסות להשיג אלכסון דומיננטי
def make_diagonally_dominant(matrix, vector):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i], matrix[j] = matrix[j], matrix[i]
            vector[i], vector[j] = vector[j], vector[i]
            if is_diagonally_dominant(matrix):
                return matrix, vector
    return matrix, vector


# פונקציה לשיטת יעקובי
def jacobi_method(matrix, vector, tolerance=0.00001, max_iterations=100):
    n = len(matrix)
    x = [0] * n  # פתרון התחלתי
    for iteration in range(max_iterations):
        x_new = [0] * n
        for i in range(n):
            s = sum(matrix[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (vector[i] - s) / matrix[i][i]

        # הצגת הפתרון באיטרציה הנוכחית
        print(f"Iteration {iteration + 1}: {x_new}")

        # בדיקת התכנסות
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            print(f"Jacobi converged in {iteration + 1} iterations.")
            return x_new
        x = x_new

    print("Jacobi did not converge.")
    return x


# פונקציה לשיטת גאוס-זיידל
def gauss_seidel_method(matrix, vector, tolerance=0.00001, max_iterations=100):
    n = len(matrix)
    x = [0] * n  # פתרון התחלתי
    for iteration in range(max_iterations):
        x_new = x[:]  # העתק של הפתרון הנוכחי
        for i in range(n):
            s1 = sum(matrix[i][j] * x_new[j] for j in range(i))
            s2 = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (vector[i] - s1 - s2) / matrix[i][i]

        # הצגת הפתרון באיטרציה הנוכחית
        print(f"Iteration {iteration + 1}: {x_new}")

        # בדיקת התכנסות
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            print(f"Gauss-Seidel converged in {iteration + 1} iterations.")
            return x_new
        x = x_new

    print("Gauss-Seidel did not converge.")
    return x


# תוכנית ראשית
if __name__ == "__main__":
    while True:
        matrixA = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
        vectorB = [2, 6, 5]

        if not is_diagonally_dominant(matrixA):
            print("Matrix is not diagonally dominant. Attempting to rearrange...")
            matrixA, vectorB = make_diagonally_dominant(matrixA, vectorB)
            if not is_diagonally_dominant(matrixA):
                print("Matrix is still not diagonally dominant. Results may not converge.")

        choice = input("Choose method: Jacobi (1), Gauss-Seidel (2), or Exit (3): ")
        if choice == "1":
            result = jacobi_method(matrixA, vectorB)
            print("Jacobi Result:", result)
        elif choice == "2":
            result = gauss_seidel_method(matrixA, vectorB)
            print("Gauss-Seidel Result:", result)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

