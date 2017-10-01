#!/usr/local/anaconda/bin/python
######################################################################
# Xin Chen
# A07
######################################################################

# I certify that the entirety of this file contains only my own
# work. I also certify that I have not shared the contents of this
# file with anyone in any form.

######################################################################
# Replace "hawkid" in the singleton tuple in the function below with
# your own hawkid USING LOWER CASE CHARACTERS ONLY.
#
# ATTENTION: Your hawkid is your login name for ICON, it is not
# your student ID number.
#
# Failure to correctly do so will result in a 0 grade.
######################################################################
def hawkid():
    return(("xchen132",))

######################################################################
# Function getBook(file) open an indicated text file and return the
# text that rules out any blank line and any line that is entirely
# made by CAPITALIZED WORDS
def getBook(file):
    f = open(file,'r')			# open and read the file
    line = f.read()			# read the whole file and return it into a string
    x = line.split('\n')		# split the line into a list and rule out the ‘\n’
    return(' '.join(([s for s in x if s != s.upper() and s!= ' '])))  # rule out CAPITAL lines and blank lines in the list and join the list into a string
    f.close()				# close the file

######################################################################
# Function cleanup(text) cleans up punctuations including parenthesis,
# commas, colons, semicolons, hyphens and both single and double
# quotes, and uses period to replace exclamatory marks and question
# marks
def cleanup(text):
    dic = {'!':'.','?':'.',',':'',':':'',';':'','“':'','”':'','‘':'','’':'',"'":'','"':'','-':'','—':'','(':'',')':''}	 # a dictionary used to pair punctuations key with empty values and exclamatory marks and question marks with period vales
    x = text.replace('’s','')			# clean up one type of possessives
    y = x.replace('s’','')			# clean up the other type of possessives
    z = y.replace("'s","")                      # in case for the possessives with straight quote
    g = z.replace("s'","")                      # reason same with the previous one
    return(''.join([dic[n] if n in dic else n for n in g]))  # clean up punctuations and replace exclamatory marks and question marks with period by using the ’key:value’ pair of dictionary

######################################################################
# Write a good comment here.
def extractWords(text):
    x = sorted([x.lower() for x in text.split()])
    return(([''.join(w for w in s if w not in '.') for s in x]))

######################################################################
# Write a good comment here.
def extractSentences(text):
    a = ''
    b = []
    for c in text:
        a = a + c
        if c == '.':
            b.append(a)
            a = ''
    return(b)

######################################################################
# Write a good comment here.
def countSyllables(word):
    pass

######################################################################
# Write a good comment here.
def ars(text):
    pass

######################################################################
# Write a good comment here.
def fki(text):
    pass

######################################################################
# Write a good comment here.
def cli(text):
    pass

######################################################################
# Reads in a book from a file and evaluates its readability. Returns
# None.
def evalBook(file='wind.txt'):
    text = cleanup(getBook(file))
    print("Evaluating {}:".format(file.upper()))
    print("  {:5.2f} Automated Readability Score".format(ars(text)))
    print("  {:5.2f} Flesch-Kincaid Index".format(fki(text)))
    print("  {:5.2f} Coleman-Liau Index".format(cli(text)))

