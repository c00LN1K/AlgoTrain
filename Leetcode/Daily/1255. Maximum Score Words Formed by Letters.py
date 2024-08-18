from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.ans = 0
        d = {chr(i + ord('a')): score[i] for i in range(26)}

        def backtracking(index, total, remain_letters):
            self.ans = max(self.ans, total)
            if index == len(words):
                return
            for j in range(index, len(words)):
                word = words[index]
                word_score = 0
                temp_remain_letters = remain_letters.copy()
                for letter in word:
                    if not temp_remain_letters.get(letter):
                        break
                    temp_remain_letters[letter] -= 1
                    word_score += d[letter]
                else:
                    backtracking(j + 1, total + word_score, temp_remain_letters)

        backtracking(0, 0, Counter(letters))
        return self.ans


print(Solution().maxScoreWords(["dog", "cat", "dad", "good"], ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                               [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
