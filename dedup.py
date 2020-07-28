import os
os.rename(r'lists/crypto.txt',r'lists/crypto-pre.txt')
# This program opens file
# input file bar.txt and removes duplicate lines and writes the
# contents to
# output file foo.txt file.
lines_seen = set()  # holds lines already seen
outfile = open('lists/crypto.txt', "w")
infile = open('lists/crypto-pre.txt', "r")
print "The file test-pre.txt is as follows"
for line in infile:
    print line
    if line not in lines_seen:  # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print "The file lists/crypto.txt is as follows"
for line in open('lists/crypto.txt', "r"):
    print line
os.remove("lists/crypto-pre.txt")
