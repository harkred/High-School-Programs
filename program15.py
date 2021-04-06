#Program to search from a csv file
import csv
def readcsv(filename):
    with open(filename) as file:
        read = csv.reader(file)
        data = [row for row in read if row != []]
        return data

def searchcsv(filename, name):
    data = readcsv(filename)
    for nam in data:
        if name == nam[1]:
            print('Student Found\n{}'.format(nam))
            break
    else:
        print('Student Not found')

filename = 'student.csv'
name = input('Enter name to be found: ')
searchcsv(filename, name)
