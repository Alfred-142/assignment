# file handling
file = open ("friends.txt", "w")

friends = ("clinton", "nephat", "susan")
for friends in friends:
    file.write(friends + " \n")
file = open ("friends.txt", "a")
file.write("james")

print("file created successfully")

#error handling
try:
    with open("friends.txt", "r") as file:
        content = file.read()
        print(f"my friends are: \n {content}")
except FileNotFoundError:
    print("file not found")
finally:
    file.close()

