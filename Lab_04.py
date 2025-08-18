# Question1
"""# Author: KierW.
# Date 18th August 2025

# Defining variables
cupcakes_per_box = 8
num_boxes = 9
num_people = 17

# Calculate result
num_cupcakes = cupcakes_per_box * num_boxes
cupcakes_leftover = num_cupcakes % num_people

#Display output
print(f"{num_boxes} boxes of cupcakes contain {num_cupcakes} cupcakes.")
print("Each person gets 4 cupcakes")
print(f"There are {cupcakes_leftover} cupcakes left over.")"""



# Question 2
"""# Author: KierW.
# Date 18th August 2025

title = "=Pythagoras Calculator="
print("=" * len(title))
print(title)
print("=" * len(title))

side_a = 4.0
side_b = 3.0

length_H = ((side_a ** 2) + (side_b ** 2)) ** 0.5
print(f"The length of the hypotenuse is {length_H}")"""



# Question 3
# Author: KierW.
# Date 18th August 2025

"""title = "=Pythagoras Calculator="
print("=" * len(title))
print(title)
print("=" * len(title))

side_a = float(input("Enter side_a: "))
side_b = float(input("Enter side_b: "))

length_H = ((side_a ** 2) + (side_b ** 2)) ** 0.5
length_H = round(length_H, 1)
print(f"The length of the hypotenuse is {length_H}")"""


# Question 4
# Author: KierW.
# Date 18th August 2025

"""title = "Cuboid Calculator"
print(f"{title}")
print("-" * (len(title)))

print("Enter the dimensions of the cuboid")
width = int(input("Width: "))
length = int(input("Length: "))
height = int(input("Height: "))

volume = width * length * height
surface_ara = (2 * width * height) + (2 * width * length) + (2 * height * length)

print(f"The volume of the cuboid is {volume}")
print(f"The surface area of the cuboid is {surface_ara}")"""



# Question 5
# Author: KierW.
# Date 18th August 2025

"""import random

# print(random.randint(1, 100))

title = "Test Mark Generator"
print(f"{title}")
print("-" * (len(title)))

test_total = int(input("Enter the test total: "))
random_num = random.randint(1, test_total)
print(f"You received {random_num} out of {test_total}")"""


# Question 6
# Author: KierW.
# Date 18th August 2025

"""import random
print("Playing craps:")
dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
total_dice = dice_1 + dice_2
print(f"You have rolled a {dice_1} and a {dice_2}")
print(f"for a total of {total_dice}")"""



# Question 7
# Author: KierW.
# Date 18th August 2025

"""import random
print("Playing craps:")
dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
total_dice = dice_1 + dice_2
print(f"You have rolled a {dice_1} and a {dice_2}")
print(f"for a total of {total_dice}")

# Roll names
num_2 = "Snake Eyes"
num_3 = "Ace Deuce"
num_4 = "Hard Four"  # when both dice show 2
num_44 = "Easy Four"
num_5 = "Fever Five"
num_6 = "Hard Six" # when both dice show 3
num_66 = "Easy Six"
num_7 = "Seven Out"
num_8 = "Hard Eight" # when both dice show 4
num_88 = "Easy Eight"
num_9 = "Nina"
num_10 = "Hard Ten"  # when both dice show 5
num_1010 = "Easy Ten"
num_11 = "Yo-leven"
num_12 = "Boxcars"

if total_dice == 2:
    print(f"This is called a {num_2}")
elif total_dice == 3:
    print(f"This is called a {num_3}")
elif total_dice == 5:
    print(f"This is called a {num_5}")
elif total_dice == 7:
    print(f"This is called a {num_7}")
elif total_dice == 9:
    print(f"This is called a {num_9}")
elif total_dice == 11:
    print(f"This is called a {num_11}n")
elif total_dice == 12:
    print(f"This is called a B{num_12}")
    
if dice_1 == dice_2:
    if total_dice == 4:
        print(f"This is called a {num_4}")
    elif total_dice == 6:
        print(f"This is called a {num_6}")
    elif total_dice == 8:
        print(f"This is called a {num_8}")
    elif total_dice == 10:
        print(f"This is called a {num_10}")
elif dice_1 != dice_2:
    if total_dice == 4:
        print(f"This is called a {num_44}")
    elif total_dice == 6:
        print(f"This is called a {num_66}")
    elif total_dice == 8:
        print(f"This is called a {num_88}")
    elif total_dice == 10:
        print(f"This is called a {num_1010}")"""