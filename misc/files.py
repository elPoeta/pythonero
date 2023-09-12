import os
# try:
#   f = open("test.txt", mode='w+', encoding='utf-8')
#   f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
# finally:
#  f.close()

# Writing to Files

with open("test.txt", mode='w', encoding='utf-8') as file:
    file.write("Test file.\n")
    file.write("----------\n\n")
    file.write("This file\n")
    file.write("contains three lines\n")

# Reading Files
with open("test.txt", mode='r', encoding='utf-8') as file:
    # read the entire file
    print(file.read())

# Directory

print(os.getcwd())
if not os.path.exists(os.getcwd() + '/' + 'testDir'):
    os.mkdir('testDir')

os.listdir()

# Remove File

os.remove("test.txt")
