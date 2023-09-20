x = int(input("type a number here: "))

if x %2 == 0:
    x *= 3
    print(x)
else:
    x *= 2
    print(x)

name = "Sheldon"

if True and True:
    print(name)

if True or False:
    print(name)

if False and False:
    print(name)

for x in range(100):
    if x %3 ==0 and x %5 ==0:
        print(f"{x} is divisible by 3 and 5")
    elif x %5 == 0:
        print(f"{x} is divisible 5")
    elif x %3 == 0:
        print(f"{x} is divisible 3")
    else:
        print(f"{x} isn't divisible by 3 or 5")

time = int(input("What time is it?"))

is_morning = time < 12

print(is_morning and "Good Morning" or "Good Evening")

