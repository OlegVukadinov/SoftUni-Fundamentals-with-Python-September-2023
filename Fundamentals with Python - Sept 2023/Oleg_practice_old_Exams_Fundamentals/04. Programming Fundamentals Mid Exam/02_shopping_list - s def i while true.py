# Initialize the grocery list
grocery_list = input().split("!")

# Function to add an item to the start of the list
def urgent(item):
    if item not in grocery_list:
        grocery_list.insert(0, item)

# Function to remove an item from the list if it exists
def unnecessary(item):
    if item in grocery_list:
        grocery_list.remove(item)

# Function to correct the name of an item
def correct(old_item, new_item):
    if old_item in grocery_list:
        index = grocery_list.index(old_item)
        grocery_list[index] = new_item

# Function to rearrange an item to the end of the list
def rearrange(item):
    if item in grocery_list:
        grocery_list.remove(item)
        grocery_list.append(item)

# Process commands until "Go Shopping!" is received
while True:
    command = input()
    if command == "Go Shopping!":
        break

    tokens = command.split()
    action = tokens[0]
    item = tokens[1]

    if action == "Urgent":
        urgent(item)
    elif action == "Unnecessary":
        unnecessary(item)
    elif action == "Correct":
        new_item = tokens[2]
        correct(item, new_item)
    elif action == "Rearrange":
        rearrange(item)

# Print the final grocery list
print(", ".join(grocery_list))
