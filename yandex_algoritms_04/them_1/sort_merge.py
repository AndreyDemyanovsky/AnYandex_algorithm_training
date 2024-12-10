
def merge_sort(data_list):

    def merge_lists(list_1, list_2):
        result_list = []
        i = 0
        j = 0
        while i != len(list_1) and j != len(list_2):
            if list_1[i] <= list_2[j]:
                result_list += [list_1[i]]
                i += 1
            else:
                result_list += [list_2[j]]
                j += 1
        return result_list + list_1[i:] + list_2[j:]

    if len(data_list) > 1:
        l = data_list[:len(data_list) // 2]
        r = data_list[len(data_list) // 2:]
        return merge_lists(merge_sort(l), merge_sort(r)) 
    return data_list


    
    

