# who pay the bill ?
from random import random
list_people = ["andi", "budi", "rispo", "gunawan", "kelvin", "stipen", "robi"]
random_number = round(random()*len(list_people))
print(f"{list_people[random_number]} yang membayar bill nya")

# treasure map
# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure (x,y and max 3,3) ? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
new_position = [int(i) for i in position.split(",")]
map[new_position[0]-1][new_position[1]-1] = "i'm here"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
