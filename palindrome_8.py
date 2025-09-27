r = input("enter string:")
r2=""
for i in r[ : :-1]:
    r2 += i
print(r2)
if r==r2:
    print("palindrome")
else:
    print("not a palindrome")