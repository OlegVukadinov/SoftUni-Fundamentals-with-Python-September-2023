number_electrons = int(input())
list_filled_shells = []

for curr_shell in range(1, number_electrons + 1):
    shell = 2 * curr_shell ** 2

    if number_electrons >= shell:
       list_filled_shells.append(shell)
       number_electrons -= shell
       if number_electrons == 0:
        break
    else:
        list_filled_shells.append(number_electrons)
        break
print(list_filled_shells)
