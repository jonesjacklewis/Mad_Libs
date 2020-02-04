f = open("MadLibOriginalFile.txt")
g = open("MadLibReplacementFile.txt", "w")

words = f.read()
words = words.split(" ")
for word in words:
    if word == "ADJECTIVE":
        replacement = str(input("Enter an Adjective: "))
        words[words.index(word)] = replacement
    elif word == "NOUN":
        replacement = str(input("Enter a Noun: "))
        words[words.index(word)] = replacement
    elif word == "VERB":
        replacement = str(input("Enter  a Verb: "))
        words[words.index(word)] = replacement

words = " ".join(words)
g.write(words)
print(words)
f.close()
g.close()
