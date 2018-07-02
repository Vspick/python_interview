# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        i = 0
        while i < len(intervals) - 1:
            cur = intervals[i]
            next = intervals[i + 1]
            if next.start > cur.end:  # 无重叠
                i += 1
            elif next.end <= cur.end:  # next被cur完全包裹
                intervals.pop(i + 1)
            else:
                new_interval = Interval(cur.start, next.end)
                intervals.pop(i + 1)
                intervals.pop(i)
                intervals.insert(i, new_interval)
        return intervals


class Solution(object):
    def merge_ans(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        merged = []

        for interval in intervals:
            if not merged or interval.start > merged[-1].end:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged


if __name__ == "__main__":
    x = [[1, 3], [2, 6], [8, 10], [15, 18]]
    input = list()
    for xx in x:
        input.append(Interval(xx[0], xx[1]))

    intervals = Solution().merge(input)
    for x in intervals:
        print(x.start, x.end)
