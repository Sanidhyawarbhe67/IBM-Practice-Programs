sentence = input("Enter a sentence: ")
words = sentence.split()

if len(words) == 0:
    print("You didn't enter any words")
else:
    biggest = words[0]

    for word in words:
        if len(word) > len(biggest):
            biggest = word

    print("The longest word is", biggest)