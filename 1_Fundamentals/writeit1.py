print("File I/O\n")
text_file = open("write_it.txt", "r+")

#Write stuff   
for s in range(0, 4):
    text_file.writelines("Line " +str(s)+ " of file created\n")
#Read stuff
for s in range(0, 4):
    print(text_file.readline()) #"Line" +str(s)+ "of file created")
text_file.close()