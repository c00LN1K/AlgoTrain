class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        left_balance = balance = 0
        ans = -1
        i = 0
        while i < len(gas):
            dif = gas[i] - cost[i]
            balance += dif
            if balance < 0:
                left_balance += balance
                balance = 0
                ans = i + 1
            i += 1
        print(left_balance, balance, ans)
        if abs(left_balance) <= balance:
            return ans
        return -1


print(Solution().canCompleteCircuit([3, 2, 5, 1, 3], [3, 4, 5, 1, 2]))
