text = input("Enter some text: ")
count = 0

for letter in text:
    if letter.isalpha() and letter.lower() not in "aeiou":
        count = count + 1

print("Consonants:", count)