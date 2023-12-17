# Create a dictionary to store contest information (contest: password)
contests = {}

# Create a dictionary to store user information (user: {contest: points})
users = {}

# Read input for contests
while True:
    line = input()
    if line == "end of contests":
        break
    contest, password = line.split(":")
    contests[contest] = password

# Read input for submissions
while True:
    line = input()
    if line == "end of submissions":
        break

    contest, password, username, points = line.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:
        if username not in users:
            users[username] = {}

        if contest not in users[username]:
            users[username][contest] = points
        else:
            if points > users[username][contest]:
                users[username][contest] = points

# Calculate total points for each user
user_total_points = {user: sum(points.values()) for user, points in users.items()}

# Find the best candidate with the most total points
best_candidate = max(user_total_points, key=user_total_points.get)
best_candidate_points = user_total_points[best_candidate]

# Print the best candidate
print(f"Best candidate is {best_candidate} with total {best_candidate_points} points.")

# Sort users by name
sorted_users = sorted(users.keys())

print("Ranking:") # Print user information in the required format
for user in sorted_users:
    print(user)
    contest_points = users[user]
    sorted_contests = sorted(contest_points, key=lambda x: (-contest_points[x], x))
    for contest in sorted_contests:
        print(f"#  {contest} -> {contest_points[contest]}")
