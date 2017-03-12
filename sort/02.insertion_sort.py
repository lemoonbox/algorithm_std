def insertion_sort(a):

    lenght = len(a)
    for i in range(1, lenght):
        for j in range(0, i):
            if a[j]>a[i]:
                a.insert(j, a.pop(i))
    return a




list1 =[100,201,6,8,4,3,23,64,42]
print(insertion_sort(list1))