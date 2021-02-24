def longest_word(lst):
    length = [len(i) for i in lst]
    return 'Longest word is {}'.format(lst[length.index(max(length))])

lst = ['Amazon', 'Facebook', 'Apple', 'Microsoft']
print(longest_word(lst))
