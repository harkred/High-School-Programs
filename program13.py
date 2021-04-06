#Recreating counter functions from collections module
def _counter(lst):
    dictionary = {}
    new = set(lst)
    for i in new:
        dictionary[i] = lst.count(i)
    return dictionary

#__main__
if __name__ == '__main__':
    lst =[1,2,3,1,2,3,4,2,12,45,2]
    print(_counter(lst))
