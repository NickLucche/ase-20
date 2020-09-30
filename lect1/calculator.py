#calculator.py

def sum(m, n):
    for _ in range(abs(n)):
        m += (1 if n>0 else -1)
    return m

def divide(m, n):
    counter = 0
    if n == 0:
        raise ZeroDivisionError()
    is_negative = m*n < 0
    n, m = abs(n), abs(m)
    while m >= n:
        m -= n
        counter += 1

    return -counter if is_negative else counter 

class FooCalculator:

    def __init__(self) -> None:
        pass
    def sum(self, m, n):
        sum(m, n)
    def divide(self, m, n):
        divide(m, n)

if __name__ == "__main__":
    import sys
    if len(sys.argv)<3:
        print("Usage python python_tutorial m n")
        exit()
    m, n = int(sys.argv[1]), int(sys.argv[2])
    print("Sum:", sum(m, n))
    print("Division:", divide(m, n))
