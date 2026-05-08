arr = [1,2,3,4,5,1,2,3]

def find_duplicates(array):
    my_dict={}
    for i in array:
        my_dict[i] = my_dict.get(i, 0) + 1
    return {k:v for k,v in my_dict.items() if v >= 2}
print(find_duplicates(arr))