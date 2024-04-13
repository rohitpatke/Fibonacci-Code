def fibonacci(n, memo={}):
   
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

def main():
    
    n = int(input("Enter the position of the Fibonacci number to find: "))
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")

if __name__ == "__main__":
    main()