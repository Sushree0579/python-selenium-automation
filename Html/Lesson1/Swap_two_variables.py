
# code here
# o(1)

# def swap_variables(a: int, b: int):
#     print(f"Before swap: a = {a} , b = {b}")  # a = 5, b = 10
#     #1
#     c = a
#     print(f"step 1: a={a}, b={b}, c={c}")
#
#     #2
#     a = b
#     print(f"step 1: a={a}, b={b}, c={c}")
#
#     #3
#     b = c
#     print(f"step 1: a={a}, b={b}, c={c}")
#
#     print(f"After swap: a = {a}, b = {b}")  # a = 10, b = 5
#     #3
#     b = c
#
#
#
# test_a = 50
# test_b = 100
# swap_variables(test_a, test_b)

def getSum(n):
    sum = 0
    for digit in str(n) :
        sum += int(digit)
        return sum
n = 12345
print(getSum(n))

def sumDigits(no): #Compute the sum of digits in all numbers from 1 to n.
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))
n = 12345
print(sumDigits(n))


def maximum(a, b, c) : #Find the max number from 3 values
    if (a >= b ) and (a >= c ) :
        largest = a
    elif (b >= a) and (b >= c) :
        largest = b
    else:
        largest = c
    return largest
a = 124
b = 21
c = 32
print(maximum(a, b, c))

# python program to count even and odd digits in a given number

def countEvenOdd(n):
    # Initialize event_count and odd_count
    even_count = 0
    odd_count = 0
    while (n > 0):
        rem = n % 10
        # if condition is true then increment even_count
        if (rem % 2 == 0):
            even_count += 1
        # increment odd count
        else:
            odd_count += 1

        n = int(n / 10)

    print("Even count : ", even_count)
    print("\nOdd count : ", odd_count)
    if (even_count % 2 == 0 and
            odd_count % 2 != 0):
        return 1
    else:
        return 0

n = 2335453;
t = countEvenOdd(n);