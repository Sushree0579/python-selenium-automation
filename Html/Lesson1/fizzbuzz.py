
# a = 5 % 3
# b = 3 % 5
# print (a)
# print (b)

#code here
#o(n)
# def fizzbuzz(n: int):
#     for i in range (1, n + 1):
#        # print("step " +str(i))
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

def factorial(number: int):
    result = 1
    for i in range(2, number + 1):
        result = result * i # result *= 1
    print(f"Factorial of {number} is {result}")

test_number = 5 # 1 * 2 * 3 * 4 * 5 = 120
factorial(test_number)



#fizzbuzz(101)