FILENAME = 'sample.txt'

vowels = ['a', 'e', 'i', 'o', 'u']

vowel = 0
consonant = 0
uppercase = 0
lowercase = 0

with open(FILENAME) as file:
    lst = [i.rstrip('\n') for i in file.readlines()]

    for word in lst:
        for letter in word:
            if letter in vowels:
                vowel += 1
            else:
                consonant += 1
            if letter.isupper():
                uppercase += 1
            else:
                lowercase += 1

print('Vowels: {}\n'.format(vowel),
      'Consonants: {}\n'.format(consonant),
      'Uppercase: {}\n'.format(uppercase),
      'Lowercase: {}\n'.format(lowercase) )
