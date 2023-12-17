version = list(map(int, input().split(".")))
version[-1] += 1
if version[-1] > 9:
   version[-1] = 0
   version[-2] += 1
if version[-2] > 9:
   version[-2] = 0
   version[-3] += 1

print(".".join(str(number) for number in version))


