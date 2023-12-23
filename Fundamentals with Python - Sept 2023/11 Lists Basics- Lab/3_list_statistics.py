n = int(input())
pos_list = []
neg_list = []

for _ in range(n):
   digit = int(input())

   if digit >= 0:
       pos_list.append(digit)
   else:
       neg_list.append(digit)
print(pos_list)
print(neg_list)
print(f"Count of positives: {len(pos_list)}")
print(f"Sum of negatives: {sum(neg_list)}")
