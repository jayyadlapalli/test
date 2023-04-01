#Mapper
import sys
#Input comes from STDIN
for line in sys.stdin:
    #Remove leading and trailing white space
    line = line.strip()
    #Split line into words
    elements = line.split()
    for element in elements:
        print element, 1
