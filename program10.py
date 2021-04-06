#Program to print frequency of a particular word in a file
def count_file(filename, word):
    count = 0
    with open(filename) as file:
        lst = [i.rstrip('\n') for i in file.readlines()]
        for line in lst:
            for wrd in line.split():
                if wrd == word:
                    count += 1
    return 'File {} has {} word {}'.format(filename, str(count), word)

#__main__
if __name__ == '__main__':
    filename = 'sample.txt'
    word = 'has'

    print(count_file(filename, word))
