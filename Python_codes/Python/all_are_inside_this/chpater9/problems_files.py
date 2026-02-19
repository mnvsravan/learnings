f=open("yoyo.txt","w")
st="Twinkel, twinkel, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky."
f.write(st)
f.close()
f=open("yoyo.txt","r")
data=f.read()
if("Twinkel" in data):
    print("Yes, 'Twinkel' is present in the file.")
else:
    print("No, 'Twinkel' is not present in the file.")


import random

def game():
    with open("high_score.txt","r") as f:
        high_score = int(f.read())

    score = random.randint(1,100)
    print("Score:", score)

    if score > high_score:
        high_score = score

    return str(high_score)

new_score = game()

with open("high_score.txt","w") as f:
    f.write(new_score)


def multiplication_table():
    for i in range(2, 20):
        with open(f"table_of_{i}.txt", "w") as f:
            for j in range(1, 10):
                f.write(f"{i} x {j} = {i*j}\n")

    for i in range(2, 20):
        with open(f"table_of_{i}.txt", "r") as f:
            print(f"Multiplication Table of {i}:")
            print(f.read())

multiplication_table()

with open("gay.txt", "w") as f:
    f.write("donkey is bad, donkey is silly, donkey is funny")

word_to_replace = "donkey"

with open("gay.txt", "r") as f:
    content = f.read()

content = content.replace(word_to_replace, "####")

with open("gay.txt", "w") as f:
    f.write(content)

words=["donkey", "silly", "funny"]
with open("gay.txt", "r") as f:
    content = f.read()
    for word in words:
        content = content.replace(word, "#"*len(word))
with open("gay.txt", "w") as f:
    f.write(content)




