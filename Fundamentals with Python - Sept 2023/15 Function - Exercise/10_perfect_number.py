def perf_number(some_number):
    sum = 0
    for divisor in range(1,some_number):
        if some_number % divisor == 0:
            sum += divisor
    if sum == some_number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

number = int(input())
perf_number(number)