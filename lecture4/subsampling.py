values = [3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6]

# I want to sample every 2nd value but only for the first half
# should be [3.2, 2.8, 6.4]

first_half_boundary = (len(values)+1)//2
subsampled = values[0 : first_half_boundary :2]
print(subsampled)