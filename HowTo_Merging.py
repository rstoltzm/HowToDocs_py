# Code is from Udemy: "The Python Mega Course: Build 10 Real World Applications" by Ardit Sulce

import glob2
from datetime import datetime

filenames = glob2.glob('file*.txt')
print('\nFor the files... \n%s\n' % filenames)

for filename in filenames:
    with open(filename) as f:
        read_data = f.read()
        print('%s reads as %s ' % (filename, read_data))

print('Merging file content...')
with open('somefile.txt', 'w') as file:
    for filename in filenames:
        with open(filename, 'r') as f:
            file.write(f.read() + "\n")
print('Merge complete\n')

print('somefile.txt reads as...\n')
with open("somefile.txt") as f:
    read_data = f.read()
    print(read_data)
