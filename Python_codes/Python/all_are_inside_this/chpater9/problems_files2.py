with open("new_file.txt", "w") as f:
    f.write('''Twinkel, twinkel, little star,
How I wonder what you are!
                Up above the world so high,
            Like a diamond in the sky.''')
with open("new_file.txt", "r") as f:
    lines = f.readlines()

line_number = 1

for line in lines:
    if "sky" in line:
        print(f"'sky' found in line {line_number}: {line}")
    line_number += 1
