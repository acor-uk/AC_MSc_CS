fileText = """4.	produce a data dictionary detailing any data structures, control structures, data storage that will be used in your program as well as any pre-defined code and assets you will include in your solution. 
5.	construct algorithm designs using Pseudocode for any methods and functions you might need.
6.	Produce test plans with test data to ensure functionality and usability of your solutions, your test plans will be implemented during the development stages.
7.	Develop a working solution that meets the requirements of the problem statement.
"""

#print(fileText)
sentences = []
sentence = ""

for chr in fileText:
    if chr == "\n":
        continue

    if chr == "\t":
        chr = " "
        
    if (chr == "." or chr == "?" or chr == "!") and not(lastChr.isnumeric()):
        print(lastChr)
        sentences.append(sentence)
        #print(sentence)
        sentence = ""
    else:
        sentence += chr
        lastChr = chr

print(sentences)

word = ""

words = []
for sentence in sentences:
    for chr in range(len(sentence)):
        if(sentence[chr].isalpha()):
            #print(sentence[chr])
            word += sentence[chr]
        elif ord(sentence[chr])<= 47 or (ord(sentence[chr]) >= 58 and ord(sentence[chr]) <= 64) or (ord(sentence[chr]) >= 91 and ord(sentence[chr]) <= 96) or ord(sentence[chr]) >= 123:
            print(ord(sentence[chr]))
            words.append(word)
            word = ""
        elif sentence[chr].isspace():
            words.append(word)
            word = ""

print(words)
print(len(words))

print(len(words[0]))