print("File I/O\n")
text_file = open("read_it.txt", "r")

for s in text_file:
    print("s: " + s)
text_file.close()