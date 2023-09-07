def get_unique_list(my_list):

    unique_set = set()
    
    result_list = []
    
    for item in my_list:
        if item not in unique_set:
            unique_set.add(item)
            result_list.append(item)
    
    return result_list

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)
print(my_list)