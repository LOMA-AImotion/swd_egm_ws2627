# ReLU(x) is ... 0 if x < 0
#            ... x if x >= 0
# type-hints: I expect an int and I give you back an int
def relu(x: int) -> int :
    print("i = ", i)
    print("x = ", x) 
    #i = 2*i this would give a local variable error
    if x < 0:
        return 0
    else:
        return x

for i in range(-10, 11):
    print(f"ReLU({i}) = {relu(i)}")