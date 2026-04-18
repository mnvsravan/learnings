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
##

with open("one.txt", "r") as f:
    data1 = f.read()

count_words = 0
count_blank = 0
count_vowels = 0
count_lower = 0
count_upper = 0

for letter in data1:
    if letter == " ":
        count_blank += 1
    elif letter.lower() in "aeiou":
        count_vowels += 1
    elif letter.islower():
        count_lower += 1
    elif letter.isupper():
        count_upper += 1
    else:
        print(f"This letter {letter} is Special")

# Word count (separate logic)
words = data1.split()
count_words = len(words)

print("Words:", count_words)
print("Blanks:", count_blank)
print("Vowels:", count_vowels)
print("Lowercase:", count_lower)
print("Uppercase:", count_upper)