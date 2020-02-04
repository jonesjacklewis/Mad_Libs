f = open("MadLibOriginalFile.txt")  # Opens the MadLibOriginalFile text file and stores in f
# Below: Opens or creates MadLibsReplacementFile text file in write mode and store in g
g = open("MadLibReplacementFile.txt", "w")  

words = f.read()  # Reads the contents of f and stores in variable words
words = words.split(" ")  # Creates a list of the words from f, splitting at commas
for word in words:  # Loops through words list
    if word == "ADJECTIVE":  # If the word is Adjective
        replacement = str(input("Enter an Adjective: "))  # Asks user to enter Adjective
        words[words.index(word)] = replacement  # Stores the replacement in the words list in the original position
    elif word == "NOUN":
        replacement = str(input("Enter a Noun: "))  # Asks user to enter Noun
        words[words.index(word)] = replacement  # Stores the replacement in the words list in the original position
    elif word == "VERB":
        replacement = str(input("Enter  a Verb: "))  # Asks user to enter Verb
        words[words.index(word)] = replacement  # Stores the replacement in the words list in the original position

words = " ".join(words)  # Creates a string from the words list, combining with a space inbetween
g.write(words)  # Writes to MadLibsReplacementFile the words string
print(words)  # Prints the words list
f.close()  # Closes file f
g.close()  # Close file g
