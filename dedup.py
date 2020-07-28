import os
os.rename(r'lists/scam.txt',r'lists/scam-pre.txt')
# This program opens file
# input file bar.txt and removes duplicate lines and writes the
# contents to
# output file foo.txt file.
lines_seen = set()  # holds lines already seen
outfile = open('lists/scam.txt', "w")
infile = open('lists/scam-pre.txt', "r")
print("The file test-pre.txt is as follows")
for line in infile:
    print(line) #line
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print("The file lists/scam.txt is as follows")
for line in open('lists/scam.txt', "r"):
    print(line) #line
os.remove("lists/scam-pre.txt")
