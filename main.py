#I'm working on javascript pp2 project at the moment,
# just quit my job so I can focus on this course thank you for the patience
course
x=2
if x>5:
    print("Greater then 5")
else:
    print("its not")
print("done with x", x)

#IF then else

if x<2:
    print("Less then 2")
elif x==2:
    print("Its twp")
else:
    print("Larger")
rawstr = input("enter a number:")
try:
    ival = int(rawstr)
except:
    ival=-1
if ival>0:
    print("Nice work", ival)
else:
    print("Not a number", rawstr)