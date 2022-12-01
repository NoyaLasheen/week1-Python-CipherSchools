a=1
while a < 10:
    print(a)
    a=a+1

# integers, complex numbers and float values are not iterableclear


name="Jatin"
for i in name:
    print(i)    
    print(type(i))

for i in range(5):
    print(i)

a=range(5)
print(a)

for i in range(5):
    print(i)
    if i == 3:
        continue

for i in range(5):
    print(i)
    if i == 3:
        break

for i in range(5):
    print(i)
    i=100
    print(i)

if True:
    pass
print("rest of the code")

for i in range(5):
    print(i)
else:
    print("something")


for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("something")


