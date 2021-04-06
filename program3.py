#Profram to read from student.dat file and search for the roll no of the student
import pickle
FILENAME = 'student.dat'

def create_file(filename, data):
    with open(filename, 'ab') as file:
        pickle.dump(data, file)
        print('File {} is made.'.format(filename)) 

def search_file(filename, roll):
    with open(filename, 'rb') as file:
        lst = []
        try:
            while True:
                b = pickle.load(file)
                lst.append(b)
        except Exception as e: pass
        lst = lst[0]
        for data in lst:
            if roll == data[0]:
                print('Student Found\n'+str(data))
                break
        else:
            print('Student not found')

#__main__
if __name__ == '__main__':
    data = [[1, 'Sonu'], [2, 'Monu'], [3, 'San']]
    create_file(FILENAME, data)
    roll = int(input('Enter roll no. : '))
    search_file(FILENAME, roll)
        
