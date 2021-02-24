FILENAME = 'sample.txt'

with open(FILENAME) as file:
    lst = [i.rstrip('\n') for i in file.readlines()]
    for line in lst:
        print(line, '#', end='')
