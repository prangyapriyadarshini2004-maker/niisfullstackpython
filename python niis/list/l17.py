L = []
print("enter how many list store")
s = int(input())

for i in range(0, s, 1):
    print("enter list", i+1, "data (comma separated)")
    data = input()
    x = list(map(int, data.split(",")))
    L.append(x)

print("elements are")
for i in range(0, len(L), 1):
    for j in range(0, len(L[i]), 1):
        print(L[i][j], end="\t")
    print()