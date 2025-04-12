list1 = [1,10,5,3,6,9,0,75,4,2,5,7]
def smallest(position: int, list1: list):
    min = list1[position]
    min_index = position
    for i in range(position,len(list1)):
        if list1[i] < min:
            min = list1[i]
            min_index = i
    return min_index

def selection_sort(list1: list) -> list:
    for i in range(0, len(list1)-1):
        min = smallest(i+1,list1)
        if list1[i] > list1[min]:
            temp = list1[i]
            list1[i] = list1[min]
            list1[min] = temp
    return list1

print(selection_sort(list1))