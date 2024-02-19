import re

text = input()

pattern = r"(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)"
while text:
    match = re.search(pattern, text)
    if match:
        valid_email = match.group(1) # защото имаме само една група

        print(valid_email)
    text = input()