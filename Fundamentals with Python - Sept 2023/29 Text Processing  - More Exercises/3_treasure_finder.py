def decrypt_message(message, key):
    decrypted_message = ""
    key_length = len(key)

    for i, char in enumerate(message):
        key_number = int(key[i % key_length])
        decrypted_char = chr(ord(char) - key_number)
        decrypted_message += decrypted_char

    return decrypted_message


def find_treasure_info(decrypted_message):
    found_treasures = []

    start_index = decrypted_message.find("&")
    while start_index != -1:
        end_index = decrypted_message.find("&", start_index + 1)
        type_of_treasure = decrypted_message[start_index + 1:end_index]

        coordinates_start = decrypted_message.find("<", end_index)
        coordinates_end = decrypted_message.find(">", coordinates_start + 1)
        coordinates = decrypted_message[coordinates_start + 1:coordinates_end]

        found_treasures.append((type_of_treasure, coordinates))

        start_index = decrypted_message.find("&", coordinates_end + 1)

    return found_treasures


# Get key input
key_sequence = input().split()

# Get lines of strings until the "find" command
lines = []
while True:
    line = input()
    if line == "find":
        break
    lines.append(line)

# Decrypt the message and find treasure information
for line in lines:
    decrypted_line = decrypt_message(line, key_sequence)
    treasures = find_treasure_info(decrypted_line)

    # Print found treasures
    for treasure in treasures:
        type_of_treasure, coordinates = treasure
        print("Found {} at {}".format(type_of_treasure, coordinates))
