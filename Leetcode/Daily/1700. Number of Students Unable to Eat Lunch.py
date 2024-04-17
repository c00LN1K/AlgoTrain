from collections import deque


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        st = deque(students)
        sandwiches = deque(sandwiches)
        n = 0
        sandwich = sandwiches.popleft()
        while n != len(st):
            student = st.popleft()
            if student == sandwich:
                n = 0
                if not sandwiches:
                    return 0
                sandwich = sandwiches.popleft()
            else:
                n += 1
                st.append(student)
        return n


print(Solution().countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
