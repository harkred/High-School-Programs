#Program to read and write into a csv file
import csv
def readcsv(filename):
    with open(filename) as file:
        read = csv.reader(file, delimiter='|')
        for row in read:
            print(row)

def writecsv(filename, data):
    with open(filename, 'w') as file:
        write = csv.writer(file)
        write.writerows(data)
        print('File written')

data = [
        [1, 'Sonu', 'Commerce', 100],
        [2, 'Monu' , 'Science', 100]
        ]
filename = 'student.csv'
writecsv(filename, data)
readcsv(filename)
