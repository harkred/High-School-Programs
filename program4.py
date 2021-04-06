#Program to update student2.dat file
import pickle

FILENAME = 'student2.dat'

def create_file(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
        print('File {} is made.'.format(filename))

def update_file(filename, roll):
    with open(filename, 'rb') as file:
        lst = []
        try:
            while True:
                b = pickle.load(file)
                lst.append(b)
        except Exception as e: pass
        lst = lst[0]
        new_lst = []
        found = 0
        for data in lst:
            new_lst.append(data)
            if roll == data[0]:
                new_lst.remove(data)
                print('Student Found\n'+str(data))
                ask = input('Would you like to update marks (y/n)? ')
                if ask == 'y':
                    marks = int(input('Marks: '))
                    data[2] = marks
                    new_lst.append(data)
                    found = 1
        if found == 1: pass
        elif found == 0 : print('Student not found')
        create_file(filename, new_lst)

#__main__
if __name__ == '__main__':
    data = data = [[1, 'Sonu', 60], [2, 'Monu', 70], [3, 'San', 70]]
    create_file(FILENAME, data)
    roll = int(input('Enter roll no. : '))
    update_file(FILENAME, roll)
