class Solution(object):
    def fullJustify(self, words, maxWidth):
        k = 0
        t = []
        ans = []
        i = 0
        while i < len(words):
            if (k + len(words[i])) <= maxWidth:
                t.append(words[i])
                k += len(words[i]) + 1
                i += 1
            else:
                if len(t) == 1:
                    ans.append(t[0] + ' ' * (maxWidth - k + 1))
                else:
                    k -= 1
                    space = ' '
                    for_space = maxWidth - k
                    space += ' ' * (for_space // (len(t) - 1))
                    extra_space = for_space % (len(t) - 1)
                    line = ''
                    for j in t:
                        line += j + space + (' ' if extra_space > 0 else '')
                        extra_space -= 1
                    ans.append(line.strip())
                k = 0
                t = []

        if len(t):
            ans.append(' '.join(t) + ' ' * (maxWidth - k + 1))

        return ans


print(Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16))