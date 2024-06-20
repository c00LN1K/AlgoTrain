class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        left = right = 0
        for el in s:
            if el == ')':
                if left:
                    left -= 1
                    stack.append(el)
            elif el == '(':
                left += 1
                stack.append(el)
            else:
                stack.append(el)
        if left == 0:
            return ''.join(stack)
        else:
            ans = []
            for el in stack[::-1]:
                if el == '(':
                    if right:
                        right -= 1
                        ans.append(el)
                elif el == ')':
                    right += 1
                    ans.append(el)
                else:
                    ans.append(el)

            return ''.join(ans[::-1])


print(Solution().minRemoveToMakeValid('))(('))
