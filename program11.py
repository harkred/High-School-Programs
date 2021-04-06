#To print out longest wordfrom a list
def longest_word(lst):
    length = [len(i) for i in lst]
    return 'Longest word is {}'.format(lst[length.index(max(length))])

#__main__
if __name__ == '__main__':
    lst = ['Amazon', 'Facebook', 'Apple', 'Microsoft']
    print(longest_word(lst))
