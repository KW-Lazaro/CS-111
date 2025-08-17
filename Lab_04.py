# Author: KierW.
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
print(f"There are {cupcakes_leftover} cupcakes left over.")