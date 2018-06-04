
def fib(N):
    n0 = 1
    n1 = 1
    for i in range(N):
        n0, n1 = n1, n0 + n1
    return n0

if __name__ == "__main__":
    for i in range(10):
        print(fib(i))
