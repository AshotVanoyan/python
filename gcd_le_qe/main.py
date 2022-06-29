from random import random
from math import floor


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def linear_equation(a, b, y):
    if a == 0 and b == y:
        return "X c R"
    if a == 0 and b == 0 and y != 0:
        return "X c O"
    if a == 0 and b != y:
        return "X c O"
    return (y - b) / a


def discriminant(a, b, c, y):
    return pow(b, 2) - 4 * a * (c - y)


def quadratic_equation(a, b, c, y):
    if a == 0:
        return linear_equation(b, c, y)

    d = discriminant(a, b, c, y)

    if d == 0:
        return -b / (2 * a)
    if d > 0:
        return [(-b + pow(d, 1 / 2)) / (2 * a), (-b - pow(d, 1 / 2)) / (2 * a)]
    if d < 0:
        d = (pow(-d, (1 / 2))) / (2 * a)
        if d == 1:
            d = 'i'
        else:
            d = str(d) + 'i'
        if b == 0:
            return [d, '-' + d]
        else:
            return [str(-b / (2 * a)) + ' + ' + d, str(-b / (2 * a)) + ' - ' + d]


# a = int(input())
# b = int(input())
# print(gcd_le_qe(a, b))
# print(gcd_le_qe(15, 85))
# print(gcd_le_qe(85, 15))
# print(gcd_le_qe(15, 0))
# print(gcd_le_qe(0, 85))


# write = open('gcd_tests.txt', 'w')
# for _ in range(100):
#     value1 = floor(random() * 100 + 1)
#     value2 = floor(random() * 100 + 1)
#     write.write(str(value1) + ' ' + str(value2) + '\n')
#
# read = open('gcd_tests.txt', 'r')
# writeResults = open('gcd_results.txt', 'w')
# for line in read:
#     number1 = line.split(' ')[0]
#     number2 = line.split(' ')[1].split('\n')[0]
#     writeResults.write('[' + number1 + ', ' + number2 + '] = ' + str(gcd(int(number1), int(number2)))+'\n')

########################################################################################################################

# a = int(input())
# b = int(input())
# y = int(input())
# linear_equation(a, b, y)
# print(linear_equation(0, 0, 0))
# print(linear_equation(0, 0, 1))
# print(linear_equation(0, 1, 1))
# print(linear_equation(0, 1, 2))
# print(linear_equation(5, 1, 11))

# write = open('linear_equation_tests.txt', 'w')
# for _ in range(100):
#     a = floor(random() * 100)-50
#     b = floor(random() * 100)-50
#     y = floor(random() * 100)-50
#     result = str(y)
#     result += ' = '
#     result += str(a) + 'x' + ' + ' + str(b) + '\n'
#     write.write(result)

# read = open('linear_equation_tests.txt', 'r')
# writeResults = open('linear_equation_results.txt', 'w')
# for line in read:
#     y = line.split(' ')[0]
#     a = line.split(' ')[2].split('x')[0]
#     b = line.split(' ')[4].split('\n')[0]
#     writeResults.write(line.split('\n')[0] + ': solution -> ' + str(linear_equation(int(a), int(b), int(y))) + '\n')

########################################################################################################################

# write = open('quadratic_equation_tests.txt', 'w')
# for _ in range(100):
#     a = floor(random() * 100) - 50
#     b = floor(random() * 100) - 50
#     c = floor(random() * 100) - 50
#     y = floor(random() * 100) - 50
#     result = str(y)
#     result += ' = '
#     result += str(a) + 'x^2' + ' + ' + str(b) + 'x' + ' + ' + str(c) + '\n'
#     write.write(result)

# read = open('quadratic_equation_tests.txt', 'r')
# writeResults = open('quadratic_equation_results.txt', 'w')
# for line in read:
#     y = line.split(' ')[0]
#     a = line.split(' ')[2].split('x^2')[0]
#     b = line.split(' ')[4].split('x')[0]
#     c = line.split(' ')[6].split('\n')[0]
#     writeResults.write(
#         line.split('\n')[0] + ': solution -> ' + str(quadratic_equation(int(a), int(b), int(c), int(y))) + '\n')

# a = int(input())
# b = int(input())
# c = int(input())
# y = int(input())
# quadratic_equation(a, b, c, y)
# print(quadratic_equation(0, 0, 0, 0))
# print(quadratic_equation(0, 0, 0, 1))
# print(quadratic_equation(0, 0, 1, 1))
# print(quadratic_equation(0, 0, 1, 2))
# print(quadratic_equation(0, 5, 1, 11))
# print(quadratic_equation(1, -4, 15, 0))
