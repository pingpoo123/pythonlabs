def calculate_avg_temp(temp_list):
    temp_sum, n = 0, 0
    for temp in temp_list:
        temp_sum += temp
        n += 1
    return temp_sum / n

def when_is_spring(temp_list):
    num_days = 0
    temp_index = -1
    i = -1
    for temp in temp_list:
        i +=1
        if temp > 0:
            num_days += 1
            if temp_index == -1:
                temp_index = i
        else:
            num_days = 0
            temp_index = -1
        if num_days == 7:
            break
    return temp_index
        