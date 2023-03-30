a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))

if a>b:
    if a>c:
        print(a,"is grater")
    else:
        print(c,"is grater")
elif b>c:
    print(b,"is grater")
else:
    print(c,"is grater")
