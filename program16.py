#stack
def is_empty(lst):
    if len(lst) == 0: return 1
    else: return 0

def push(lst, element):
    lst.append(element)
    return 'Push complete'

def pop(lst):
    if is_empty(lst) == 1:
        return 'Underflow'
    else:
        lst.pop()
        return 'Pop complete'

def peek(lst):
    for i in range(len(lst)):
        if i == 0:
            print(lst[i]+'<--')
        else:
            print(lst[i])

def display(lst):
    return lst

#__main__
if __name__ == '__main__':
    print("""
Choose your command:-
q - Quit
push -Push
pop -Pop
peek -Peek
show -Display
""")
    stack = []
    while True:
        cmd = input('Enter command: ')
        if cmd == 'q': break
        elif cmd == 'push':
            n = input('Enter element to be pushed: ')
            print(push(stack, n))
        elif cmd == 'pop': print(pop(stack))
        elif cmd == 'peek': peek(stack)
        elif cmd == 'show': print(display(stack))
        else: print('Enter a valid command')
