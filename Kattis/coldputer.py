n = input()
line = input()
count = int(0)

for x in line:
    if x == "-":
        count += 1

print(count)
