# originally coded by me with extra logical steps; refined through google-fu to get shorter code.

def fibonacci(length):
    fib_length = length
    n1, n2 = 0, 1
    if length == 1:
        print(n1)
    else:
        while fib_length > 0:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            fib_length -= 1


def lucas(length):
    luc_length = length
    n1, n2 = 2, 1
    if length == 1:
        print(n1)
    else:
        while luc_length > 0:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            luc_length -= 1


print("Fibonacci to a given value (here 5)")
fibonacci(5)
print("Lucas to a given value (here also 5)")
lucas(5)
