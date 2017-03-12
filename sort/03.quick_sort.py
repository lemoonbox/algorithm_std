

def quick_sort(a, left, right):
    if type(a) != type([]):
        raise TypeError("parameter must be list")
        return

    if (left >= right):
        return
    pvtindex = left
    lowindex = left+1
    hightindex = right

    while lowindex<hightindex and lowindex != hightindex:
        if a[lowindex]>a[hightindex]:
            a[lowindex],a[hightindex] = a[hightindex],a[lowindex]
        if a[lowindex]<a[pvtindex]:
            lowindex += 1
        if a[hightindex] > a[pvtindex]:
            hightindex -= 1

    if a[hightindex]<a[pvtindex]:
        a[hightindex], a[pvtindex] = a[pvtindex], a[hightindex]

    quick_sort(a, left, hightindex-1)
    quick_sort(a, hightindex+1, right)

    return a


unsored_list = [6,4,7,2,5,9,8,1,3]


print(quick_sort(unsored_list, 0, len(unsored_list)-1))









