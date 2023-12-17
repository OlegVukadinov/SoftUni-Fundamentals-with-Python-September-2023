words_list = input().split()

command = input()

while not command == "Stop":
    action = command.split()[0]

    if action == "Delete":
        index = int(command.split()[1])
        if index + 1 in range(len(words_list)):
            words_list.remove(words_list[index + 1])

    elif action == "Swap":
        word_1 = command.split()[1]
        word_2 = command.split()[2]
        if word_1 in words_list and word_2 in words_list:
            index1 = words_list.index(word_1)
            index2 = words_list.index(word_2)
            words_list[index1], words_list[index2] = words_list[index2], words_list[index1]

    elif action == "Put":
        word_1 = command.split()[1]
        index = int(command.split()[2])
        if 0 <= index - 1 <= len(words_list):
            words_list.insert(index - 1, word_1)

    elif action == "Sort":
        words_list.sort(reverse=True)

    elif action == "Replace":
        word_1 = command.split()[1]
        word_2 = command.split()[2]
        if word_2 in words_list:
            i = words_list.index(word_2)
            words_list[i] = word_1

    command = input()

print(' '.join(words_list))