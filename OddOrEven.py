#Part 1
number = int(input("Enter a number: "))
if number % 4 == 0:
    print("The number is a multiple of 4 and is also even")
elif  number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Part 2
print("")
num = int(input("Enter a number: "))
check = int(input("Enter a check value to divide by: "))

if num % check == 0:
    print("%d divides evenly by %d" % (num, check))
else:
    print("%d does not divide evenly by %d" % (num, check))
