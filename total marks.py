rno=int(input("Roll no: "))
name=input("Student Name: ")
s1=int(input("Subject no 1: "))
s2=int(input("Subject no 2: "))
s3=int(input("Subject no 3: "))

total=s1+s2+s3
per=total/3

print("Student Name: ",name)
print("Roll no: ",rno)
print("Total Marks: ",total)
print("Percentage: ",per)

if per>70:
    print("Distection")
elif per>60:
    print("First Class")
elif per>50:
    print("Second Class")
elif per>40:
    print("Pass Class")
else:
    print("Fail")
