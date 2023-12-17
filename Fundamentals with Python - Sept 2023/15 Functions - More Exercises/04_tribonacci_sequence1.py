def tribonacci(n):
    if n <= 0:
        return []

    if n == 1:
        return [1]

    if n == 2:
        return [1, 1]

    tribonacci_sequence = [1, 1, 2]

    for i in range(3, n):
        next_tribonacci = tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 3]
        tribonacci_sequence.append(next_tribonacci)
    return tribonacci_sequence

def print_tribonacci_sequence(n):
    tribonacci_sequence = tribonacci(n)
    print(" ".join(map(str, tribonacci_sequence)))


n = int(input())
print_tribonacci_sequence(n)
