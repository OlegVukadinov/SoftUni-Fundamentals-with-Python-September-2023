results = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break

    if "banned" in command:
        username, ban_command = command.split("-")
        if username in results:
            del results[username]  # Remove the user from the contest
            continue

    data = command.split("-")
    username = data[0]
    language = data[1]
    points = int(data[2])

    if username not in results:
        results[username] = points
    else:
        if points > results[username]:
            results[username] = points

    if language not in submissions:
        submissions[language] = 1
    else:
        submissions[language] += 1

print("Results:")
for username, points in results.items():
    print(f"{username} | {points}")

print("Submissions:")
for language, submissions_count in submissions.items():
    print(f"{language} - {submissions_count}")



