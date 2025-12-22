# Method 1: Using if-else statements 1
# Method 2 : Using Calendar Mode

year=2000
if year%4==0 and year%100!=0 or year%400==0:
    print("leap year")
else:
    print("not leap year")

#2.
m=int(input("enter the year:"))
if m%4==0 and m%100!=0 or m%400==0:
    print('leap year')
else:
    print("not leap year")




