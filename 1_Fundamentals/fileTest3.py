fileText = """4.	produce a data dictionary detailing any data structures, control structures, data storage that will be used in your program as well as any pre-defined code and assets you will include in your solution. 
5.	construct algorithm designs using Pseudocode for any methods and functions you might need.
6.	Produce test plans with test data to ensure functionality and usability of your solutions, your test plans will be implemented during the development stages.
7.	Develop a working solution that meets the requirements of the problem statement.
"""

#print(fileText)
sentences = [] # create a list to store the sentences
sentence = "" # initialise a variable to store the current sentence

for chr in fileText:
    if chr == "\n":
        continue # skip the newline character
    
    if chr == "\t":
        chr = " " # change the tab character to a space
        
    if (chr == "." or chr == "?" or chr == "!") and not(lastChr.isnumeric()):
        #print(lastChr) 
        sentences.append(sentence) # if the character is a full stop, question mark or exclamation mark, add the sentence to the list
        #print(sentence)
        sentence = "" # reset the sentence variable
    else:
        sentence += chr # add the character to the sentence
        lastChr = chr # store the last character to check if it was a number

print(sentences) # check that the sentences have stored correctly

word = "" # initialise a variable to store the current word
words = [] # create a list to store the words
wordsCount = 0 # initialise a variable to store the total number of words

for sentence in sentences: # loop through the sentences
    for chr in range(len(sentence)-1): # loop through the characters in the sentence
        if(sentence[chr].isnumeric()): 
            sentence = sentence.replace(sentence[chr],"") # remove any numbers from the sentence
    sentence = sentence.replace(".","") # remove full stops / they should already be gone
    sentence = sentence.replace(",","") # remove commas
    sentence = sentence.replace(";","") # remove semi-colons / should later repeat for other punctuation
    sentence = sentence.rstrip() # remove any trailing spaces
    sentence = sentence.lstrip() # remove any leading spaces
    temp = sentence.split(" ") # split the sentence into words and add to a temporary list
    wordsCount += len(temp) # add the number of words in the sentence to the total
    #print(wordsCount)
    words.append(temp) # add the list of words to the words list
    
print(words[0]) # check the first sentence in the words list
print(f"Words in Sentence: {len(words[0])}") # check the number of words in the first sentence
print(f"Total Words: {wordsCount}") # check the total number of words
lengths = [] # create a list to store the lengths of the words

for sentence in words: # loop through the sentences
    for word in sentence: # loop through the words
        lengths.append(len(word)) # add the length of the word to the lengths list
    
print(lengths) # check all the word lengths
print(f"Total Words: {len(lengths)}") # check the total number of words

maxLen = max(lengths) # set the maximum word length to the maximum value in the lengths list
minLen = min(lengths) # set the minimum word length to the minimum value in the lengths list
print(f"Max Word Length: {maxLen}. Min Word Length: {minLen}") #print the max and min word lengths
meanLen = sum(lengths)/len(lengths) # calculate the mean word length
print(f"Mean Word Length: {meanLen :.2f}") # print the mean word length to 2 decimal places
lengthCount = [] # create a list to store the number of words of each length

for i in range(minLen,maxLen+1):
    numWords = lengths.count(i)
    lengthCount.append([i,numWords]) # add the length and number of words of that length to the lengthCount list
    print(f"Words of Length {i}: {numWords}") # print the number of words of each length

print(lengthCount) # check the lengthCount list