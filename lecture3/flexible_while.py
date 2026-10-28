k = int(input("k?"))

i = 0
while i < k + 1: 
    print(i)
    i = i + i

# would work with for? No!
for i in range(1, k+1):
    print(i)
    i = i + i 