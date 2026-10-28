guests = []
guest_command = input("Please enter a guest name (or 'done' to finish): ")
while guest_command != "done":
    guests.append(guest_command)
    guest_command = input("Please enter a guest name (or 'done' to finish): ")

print("The guests are:", guests)