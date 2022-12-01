a = False
if a == True:
    print('the value is true')
print('end')

if a == True:
    print('this value is true')
else:
    print('this value is false')

a=5

if a == 3 :
    print('this value is 3')
elif a == 5:
    print('this value is 5')
else:
    print('this value is not 3 nor 5')

# can profile A access profile B ?
# a = isFriend
# b = isBlocked
# c = isMarkZuckerburg

# if the above condition is true input 1
# if the above the condition is false input 0

a = int(input())
b = int(input())
c = int(input())

if a==0 and b==0 and c==0:
    print("Profile cannot be accesed")
elif a==0 and b==0 and c==1:
    print("Profile can be accesed")
elif a==0 and b==1 and c==1:
    print("Profile can be accesed")
elif a==0 and b==1 and c==0:
    print("Profile cannot be accesed")
elif a==1 and b==0 and c==1:
    print("Profile can be accesed")
elif a==1 and b==0 and c==0:
    print("Profile can be accesed")
elif a==1 and b==1 and c==0:
    print("Profile cannot be accesed")
elif a==1 and b==1 and c==1:
    print("Profile can be accesed")

