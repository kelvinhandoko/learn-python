"""
 You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
 Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
"""
height = int(input("how much height is that? "))
width = int(input("how much width is that? "))


def calculate(height, width):
    hasil = height * width / 5
    return hasil


hasil = calculate(height, width)
print(f"you'll need {round(hasil)} cans of paint")
