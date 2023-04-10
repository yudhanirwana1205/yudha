listi = [1,4,5,6,2,4]
listi.reverse
print(listi)

listi = [1,4,5,6,2,4]

assert([ x for x in listi if x == 4]) == [1,5,6,2]

assert([x for x in listi if x ==4]) == [4,4]