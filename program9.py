#File copying program
def copy_files(original_file, copy_file):
    with open(original_file) as file1:
        lst = [i for i in file1.readlines()]
    with open(copy_file, 'w') as file2:
        file2.writelines(lst)
    print('File copied')

original_file = 'sample.txt'
copy_file = 'copy.txt'

copy_files(original_file, copy_file)
