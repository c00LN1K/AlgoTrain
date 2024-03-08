class Solution(object):
    def candy(self, ratings):
        if len(ratings) == 1:
            return 1
        res = 1 if ratings[0] < ratings[1] else 0
        last_value = 1
        start_value = 1
        start = -1
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                if start != -1:
                    dif = i - start
                    res += (dif + 1) / 2 * dif
                    if start:
                        res += -start_value if dif > start_value else -dif
                    last_value = 1
                    start = -1
                last_value += 1
                res += last_value
            elif ratings[i - 1] > ratings[i]:
                if start == -1:
                    start = i - 1
                    start_value = last_value
            elif ratings[i - 1] == ratings[i]:
                if start != -1:
                    dif = i - start
                    res += (dif + 1) / 2 * dif
                    if start:
                        res += -start_value if dif > start_value else -dif
                    start = -1
                last_value = 1
                res += last_value
            print(res)

        if start != -1:
            dif = len(ratings) - start
            res += (dif + 1) / 2 * dif
            if start:
                res += -start_value if dif > start_value else -dif

        return int(res)


print(Solution().candy([1,3,2,2,1]))
