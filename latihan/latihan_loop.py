# average height
student_heights = input("Input a list of student heights ").split()
hasil = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    hasil += student_heights[n]
length = len(student_heights)
print(round(hasil / length))

# find the highest score
student_scores = input("Input a list of student scores ").split()
hasil = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    hasil = student_scores[n] if hasil < student_scores[n] else hasil
print(f"The highest score is {hasil}")

# sum all even number to 100
hasil = 0
for i in range(1, 101):
    if i % 2 == 0:
        hasil += i
print(hasil)

