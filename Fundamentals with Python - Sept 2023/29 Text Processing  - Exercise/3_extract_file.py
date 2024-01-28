filepath = input().split("\\")
filename_extension = filepath[-1]
filename, extension = filename_extension.split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")
