PATH = '08. Files/file.txt'

# files = open(PATH, 'w')

# print(
#     f'files: {files}\nName: {files.name}\nIs closed: {files.closed}\nMode: {files.mode}')
# files.write(f'This is a test!\n')
# files.write(f'Python the best programming language.\n')
# files.close()

# files = open(PATH, 'a')
# files.write(f'A also like C#!\n')
# files.close()


files = open(PATH, 'r+')
text = files.readline()
# read = files.read(9)
read = files.read()
files.close()

print(text)
# print(read)
