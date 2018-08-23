# Write a function to calculate pow(int x, int y), 0 <= x <= 9, and 0 <= y <= 99
# Requirement: print out the correct result on screen
def pow(x, y):
    if x == 0 and y != 0:
        return 0
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        half_y = y // 2
        rest_y = y % 2
        return pow(x, half_y) * pow(x, half_y) * pow(x, rest_y)


def pow(x, y):
    result = [1]
    for i in range(0, y):
        result = multi(x, result)
    return result


# long long 2^64
def multi(x, list_y):
    len_y = len(list_y)
    add = 0
    result = []
    for i in range(len_y - 1, -1, -1):
        num = x * list_y[i] + add
        add = num // 10
        rest = num % 10
        result.append(rest)
    if add != 0:
        result.append(add)
    return result[::-1]



# INPUT: N sorted lists
# Eg, [1, 2, 3], [0, 1, 2], [0, 0, 3], [4]
# OUTPUT: merged sorted list
# => [0, 0, 0, 1, 1, 2, 2, 3, 3, 4]


def merge_sorted_lists(sorted_lists):
    sorted_lists_len = len(sorted_lists)
    if sorted_lists_len <= 1:
        return sorted_lists
    elif sorted_lists_len == 2:
        merge_list = []
        i = 0, j = 0
        list0_len = len(sorted_lists[0])
        list1_len = len(sorted_lists[1])
        while i < list0_len and j < list1_len:
            if sorted_lists[0][i] <= sorted_lists[1][j]
                merge_list.append(sorted_lists[0][i])
                i += 1
            else:
                merge_list.append(sorted_lists[1][j])
                j += 1
        while i < list0_len:
            merge_list.append(sorted_lists[0][i])
            i += 1
        while j < list1_len:
            merge_list.append(sorted_lists[1][j])
            j += 1
        return merge_list
    else:
        mid = int(sorted_lists_len / 2)
        merge_list1 = merge_sorted_lists(sorted_lists[0:mid])
        merge_list2 = merge_sorted_lists(sorted_lists[mid + 1:])
        return merge_sorted_lists([merge_list1, merge_list2])


# Compute cubic root of a float value, using only +, -, *, /
def cal_cubic_root(v):
    result = 0
    abs_v = v if v >= 0 else -v
    l = 0
    r = v if v >= 1 else 1
    while l < r and (abs_v - result * result * result) > 1e-9:
        mid = (l + r) / 2
        if mid * mid * mid < abs_v:
            l = mid
            result = l
        elif mid * mid * mid > abs_v:
            r = mid
            result = l
        else:
            result = mid
            break
    if v < 0:
        result = -result

    return result



