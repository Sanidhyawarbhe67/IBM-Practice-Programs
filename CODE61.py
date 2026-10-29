text = input("Enter some text: ")
count = 0

for letter in text:
    if letter == " ":
        count = count + 1

print("Spaces:", count)