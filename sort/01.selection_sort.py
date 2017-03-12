def selection_sort(unsored):
    if type(unsored) != type([]):
        raise  TypeError("parameter(1) is must be list")
        return

    lenght = len(unsored)
    for i in range(lenght):
        indexmin= i
        for j in range(i+1, lenght):
            if unsored[indexmin] > unsored[j]:
                indexmin = j
        unsored[i], unsored[indexmin] = unsored[indexmin], unsored[i]
    return unsored




list1 =[100,201,6,8,4,3,23,64,42]
print(selection_sort(list1))






