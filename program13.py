def _counter(dictionary, lst):
    new = set(lst)
    for i in new:
        dictionary[i] = lst.count(i)
    return dictionary

dictionary = {}
lst =[1,2,3,1,2,3,4,2,12,45,2]
print(_counter(dictionary, lst))
