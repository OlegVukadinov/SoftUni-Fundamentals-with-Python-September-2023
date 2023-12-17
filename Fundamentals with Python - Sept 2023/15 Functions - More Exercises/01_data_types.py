def data(some_text1, some_text2):
    if some_text1 == "int":
        return int(some_text2) * 2
    if some_text1 == "real":
        result = f"{float(some_text2) * 1.5:.2f}"
        return result
    if some_text1 == "string":
        return f"${some_text2}$"


text1 = input()
text2 = input()

print(data(text1, text2))