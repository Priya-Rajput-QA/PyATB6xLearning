# Write a program to take a user age and
# let him know if he can go the club.
# 21
# i/p - age, int
# o / p - String (result -> Can go to club or not.

age = int(input("Enter the age:").strip())
if age <=0 or age >130:
    print("Enter the valid age")
else:
    if age>=21:
        print("Yes, you can go to the club")
    else:
        print("No, you can not go to the club")

