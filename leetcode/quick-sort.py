
def quick_sort(nums, left, right):

    if left >= right:
        return nums
    base = nums[left]
    low = left
    high = right
    while left < right:
        while nums[right] >= base and left < right:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
        while nums[left] <= base and left < right:
            left += 1
        nums[left], nums[right] = nums[right], nums[left]
    quick_sort(nums, low, left - 1)
    quick_sort(nums, left + 1, high)


def quick_sort_ans(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]  # 注意，不用交换两个的顺序，只赋值一边即可
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


if __name__ == "__main__":
    a = [9, 7, 2, 6, 0, 7, 3]
    quick_sort_ans(a, 0, len(a) - 1)
    print(a)
