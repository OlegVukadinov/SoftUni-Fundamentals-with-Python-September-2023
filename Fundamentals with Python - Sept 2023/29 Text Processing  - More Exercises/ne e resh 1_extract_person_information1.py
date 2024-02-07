n = int(input())
name = ""
age = ""
for curr_n in range(n):
    text = input().split()
    for curr_word in text:
        if curr_word.startswith("@"):
            if curr_word.endswith("|"):
              name = curr_word[1:-1]
        if curr_word.startswith("#"):
            if curr_word.endswith("*"):
              age = curr_word[1:-1]
        
    print(f"{name} is {age} years old.")