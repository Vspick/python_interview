class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasks_queues = {}
        for task in tasks:
            if task not in tasks_queues:
                tasks_queues[task] = 1
            else:
                tasks_queues[task] += 1
        time = 0
        while tasks_queues:
            sorted_tasks = sorted(tasks_queues.items(), key=lambda x:x[1], reverse=True)
            tasks_queues_len = len(tasks_queues.keys())
            for i in range(n + 1):
                if not tasks_queues:
                    break
                if i < tasks_queues_len:
                    k = sorted_tasks[i][0]
                    tasks_queues[k] -= 1
                    print(k, tasks_queues[k])
                    if tasks_queues[k] == 0:
                        tasks_queues.pop(k)
                time += 1
                print(time)
        return time


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        size = len(tasks)
        if n == 0:
            return size

        # 统计每个任务需要执行的次数
        ORD_A = ord('A')
        freqs = [0] * 26
        for task in tasks:
            freqs[ord(task) - ORD_A] += 1

        # 找出次数最多的任务需要执行的次数
        freqs.sort(reverse=True)
        freqmax = freqs[0]

        freqmaxcnt = 0
        for freq in freqs:
            if freq == freqmax:
                freqmaxcnt += 1

        return max(size, (freqmax - 1) * (n + 1) + freqmaxcnt)  # 数学公式没看懂？

    '''
        找出出现次数最多的任务，这几个任务之间的间隔为n：如,n=2，A[][]A[][]A[]
        然后逐渐插入剩余的 A[B][]A[B][]A;  A[B][C]A[B][]A; A[B][C]A[B][D]A; A[B][C]EA[B][D]A 
        全部往空位插，不够再补位，插入方式为找空插，顺序什么的随意了
        出现次数最多的字母为多个，则并一起AB[]AB[]AB
        '''


if __name__ == "__main__":
    obj = Solution()
    time = obj.leastInterval(["A","A","A","B","B","B"], 2)
    print(time)

