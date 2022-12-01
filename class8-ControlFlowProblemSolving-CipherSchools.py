n=int(input())
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()
print("\n")

for i in range(n):
    for j in range(n):
        print(max(i+1, j+1, n-i, n-j),end=" ")
    print()
print("\n")

for i in range(n):
    for j in range(n):
        print(max(i,j,end=" "))
    print()
print("\n")

