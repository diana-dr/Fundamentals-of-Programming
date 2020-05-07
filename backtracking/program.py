"""
12) Consider the natural number n (n<=10) and the natural numbers 𝑎1, …, 𝑎𝑛. Determine all the
possibilities to insert between all numbers 𝑎1, …, 𝑎𝑛 the operators + and – such that by evaluating the
expression the result is positive.
"""


def consistent(s, n):
    if len(s) >= n:
        return False

    return True


def solution(x, n, data):
    result = data[0]

    if len(x) != n - 1:
        return False

    for i in range(n - 1):
        if x[i] == "+":
            result = result + data[i + 1]
        else:
            result = result - data[i + 1]

    if result > 0:
        return result


def solution_found(x, n, data):
    summ = 0
    for i in range(n):
        if x[i - 1] == '+':
            summ += data[i]
        else:
            summ -= data[i]

    result = []
    for i in range(n):
        result.append(x[i-1] + ' ' + str(data[i]))

    result.append(summ)

    print(result)


def backtracking_iterative(n, data):
    operators = [-1, "-", "+"]
    x = [-1]

    while len(x) > 0:
        chosen = False
        while not chosen and operators.index(x[-1]) < len(operators) - 1:
            x[-1] = operators[operators.index(x[-1]) + 1]
            chosen = consistent(x, n)

        if chosen:
            if solution(x, n, data):
                solution_found(x, n, data)
            x.append(-1)

        else:
            x = x[:-1]


def backtracking_recursive(x, n, data):
    operators = ["-", "+"]

    for i in operators:
        x.append(i)
        if consistent(x, n):
            if solution(x, n, data):
                solution_found(x, n, data)
            backtracking_recursive(x, n, data)

        x.pop()


list = [-1, -5, -90, -2, -30, 100]

print("Backtracking iterative: ")
backtracking_iterative(6, list)
print("\nBacktracking recursive: ")
backtracking_recursive([], 6, list)


