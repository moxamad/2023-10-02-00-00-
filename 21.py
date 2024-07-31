import random

left=random.randint(3, 20)

right = ''
print(left)
for i in range(1, left):
    for j in range(i, left):
        if left % (i + j) == 0:
            if str(j) == str(i):
                continue
            right = right + str(i) + str(j)

print(right)