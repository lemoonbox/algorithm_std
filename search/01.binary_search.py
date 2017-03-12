


def binary_search(list, target, low=0, hight=0):


    mid = int((low+hight)/2)

    if list[mid] == target or low >= hight:
        return mid

    if list[mid]>target:
        mid =binary_search(list, target, low, mid-1)
    else :
        mid =binary_search(list, target, mid+1, hight)

    return mid






number_list = [1,2,4,5,6,7,20,33]

print(binary_search(number_list, 2, 0, len(number_list)-1))