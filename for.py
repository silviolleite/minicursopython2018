for x in "Silvio":
    print(x, end=" * ")


def fibonacci(n):
    if n == 1:
        print(n)
    print(n = n + fibonacci(n+1))

fibonacci(1)

