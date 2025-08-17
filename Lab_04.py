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

import random
print("Playing craps:")
dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
total_dice = dice_1 + dice_2
print(f"You have rolled a {dice_1} and a {dice_2}")
print(f"for a total of {total_dice}")