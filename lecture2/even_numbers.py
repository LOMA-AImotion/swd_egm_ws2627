# ask for k
# iterate from 1 to k, show just even numbers

k = int(input("Enter number k"))
for i in range(1, k+1):
    if i % 2 == 0: # test for even
        print(i)

# step version
print("-"*20)
for i in range(2, k+1, 2):
    print(i)