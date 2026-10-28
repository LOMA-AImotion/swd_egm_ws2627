# read k
# from 1 up until k, build a set that contains
# # for every i, a tuple i and i"x" characters  
k = int(input("k?"))
overall = set() # wish it was {} ... but that would be a dict

for i in range(1, k+1):
    new_tuple = (i, "x"*i)
    # add this to a set?
    overall.add(new_tuple) # not append, no sequence here

print(overall)

print("-"*50)
overall = {(i, "x"*i) for i in range(1, k+1)}
print(overall)