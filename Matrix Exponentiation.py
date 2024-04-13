def matrix_mul(A, B):
    """
    Multiplies two 2x2 matrices.
    """
    C = [[0, 0], [0, 0]]
    C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return C

def matrix_power(A, n):
    """
    Raises a 2x2 matrix to the power of n.
    """
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:
        return A
    else:
        B = matrix_power(A, n//2)
        C = matrix_mul(B, B)
        if n % 2 == 0:
            return C
        else:
            return matrix_mul(A, C)

def fibonacci(n):
    """
    Finds the nth Fibonacci number using the matrix exponentiation method.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        A = [[1, 1], [1, 0]]
        F = matrix_power(A, n-1)
        return F[0][0]

def main():
    n = int(input("Enter the position of the Fibonacci number to find: "))
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")

if __name__ == "__main__":
    main()