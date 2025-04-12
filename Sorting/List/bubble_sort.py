def bubble_sort(my_list: list) -> list:
    for i in range(len(my_list)):
        for k in range(len(my_list)-1):
            if my_list[k] > my_list[k+1]:
                temp = my_list[k]
                my_list[k] = my_list[k+1]
                my_list[k+1] = temp
    
    return my_list

my_list = [1,4,2,5,7,3,1,5,7,3]
print(bubble_sort(my_list))