# coding=utf-8
"""
当前节点 i
其父节点 (i - 1) // 2
子节点   (2 * i + 1), (2 * i + 2)
"""


def heap_sort_asc(l):
    def max_heapify(root_index, end_index):
        max_child_index = root_index * 2 + 1
        if max_child_index + 1 <= end_index:
            if l[max_child_index + 1] > l[max_child_index]:
                max_child_index += 1
        if l[max_child_index] > l[root_index]:
            l[max_child_index], l[root_index] = l[root_index], l[max_child_index]

    for end_index in range(len(l) - 1, 0, -1):    # 当前堆的末尾元素下标
        max_root_index = (end_index - 1) // 2     # 最大父节点下标
        for root_index in range(max_root_index, -1, -1):  # 从大到小调整所有非叶子节点
            max_heapify(root_index, end_index)
        l[0], l[end_index] = l[end_index], l[0]


def heap_sort_desc(l):
    def max_heapify(root_index, end_index):
        max_child_index = root_index * 2 + 1
        if max_child_index + 1 <= end_index:
            if l[max_child_index + 1] < l[max_child_index]:
                max_child_index += 1
        if l[max_child_index] < l[root_index]:
            l[max_child_index], l[root_index] = l[root_index], l[max_child_index]

    for end_index in range(len(l) - 1, 0, -1):
        max_root_index = (end_index - 1) // 2
        for root_index in range(max_root_index, -1, -1):
            max_heapify(root_index, end_index)
        l[0], l[end_index] = l[end_index], l[0]


def find_kth_min(l, k):
    def heap_min(r, e):
        child = 2 * r + 1
        if child + 1 <= e and l[child + 1] < l[child]:
            child += 1
        if l[child] < l[r]:
            l[r], l[child] = l[child], l[r]

    for e in range(len(l) - 1, len(l) - k - 1, -1):
        max_r = (e - 1) // 2
        for r in range(max_r, -1, -1):
            heap_min(r, e)
        l[e], l[0] = l[0], l[e]
    return l[-k]


if __name__ == "__main__":
    l = [6, 5, 2, 8, 9, 7, 7, 3, 1, 9, 0]
    print(l)
    r = find_kth_min(l, 5)
    print r
    print(l)
