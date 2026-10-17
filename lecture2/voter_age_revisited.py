user_name = input("Please enter your name: ")
user_age = int(input("Please enter your age: "))

voter_age = 18
if user_age > voter_age:
    print(f"Hello {user_name}, you have been eligible to vote for {user_age - voter_age} years.")
elif user_age == voter_age:
    print(f"Hello {user_name}, congratulations! It's your first time voting.")
else:
    print(f"Hello {user_name}, you will be eligible to vote in {voter_age - user_age} years.")    
