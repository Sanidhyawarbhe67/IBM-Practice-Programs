text = input("Enter some text: ")
count = 0

for letter in text:
    if letter.lower() in "aeiou":
        count = count + 1

print("Vowels:", count)