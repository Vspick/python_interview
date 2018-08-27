# coding=utf-8
"""
当前节点 i
其父节点 (i - 1) // 2
子节点   (2 * i + 1), (2 * i + 2)

求最小的k个数要用大顶堆
"""


def fix_down(l, root, heap_len):
    cur = root
    child = 2 * cur + 1
    while child < heap_len:
        if child + 1 < heap_len and l[child + 1] > l[child]:
            child = child + 1
        if l[cur] < l[child]:
            l[cur], l[child] = l[child], l[cur]
            cur, child = child, 2 * child + 1
        else:
            break


def create_heap(l, s, e):
    heap_len = e - s + 1
    max_non_leaf_node = (heap_len - 1) // 2
    for i in range(max_non_leaf_node, s - 1, -1):
        fix_down(l, i, heap_len)


def heap_sort(l):
    create_heap(l, 0, len(l) - 1)
    heap_len = len(l)
    while heap_len > 1:
        l[heap_len - 1], l[0] = l[0], l[heap_len - 1]
        heap_len -= 1
        fix_down(l, 0, heap_len)


def top_k_min(l, k):
    create_heap(l, 0, k - 1)
    for i in range(k, len(l)):
        if l[i] < l[0]:
            l[0], l[i] = l[i], l[0]
            fix_down(l, 0, k)
    return l[0:k]


if __name__ == "__main__":
    l = [9, 8, 3, 2, 4, 5, 6, 8, 0, 1, 3]
    print(l)
    heap_sort(l)
    print(l)
    l = [9, 8, 3, 2, 4, 5, 6, 8, 0, 1, 3]
    res = top_k_min(l, 3)
    print res
