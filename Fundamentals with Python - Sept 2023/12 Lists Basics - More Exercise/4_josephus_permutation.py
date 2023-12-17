numbers_people = input().split()
k = int(input())

executions = []
current_position = 0

while len(numbers_people) > 0:
    current_position = (current_position + k - 1) % len(numbers_people)
    executed_men = numbers_people.pop(current_position)
    executions.append(executed_men)

print('[' + ','.join(executions) + ']')
