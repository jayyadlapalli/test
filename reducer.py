#Reducer
import sys
count = 0
summation = 0
#Read standard input
for line in sys.stdin:
    try:
        left_side = line.strip().split()[0]
        right_side = line.strip().split()[1]
        sum_int_val = int(left_side)
        count_int_val = int(right_side)
        count += count_int_val
        summation += sum_int_val
    except ValueError:
        pass
#Prints interger average for values in the file
print( summation / count )
