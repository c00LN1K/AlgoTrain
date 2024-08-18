from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        formula = formula + ')'

        def get_count(i):
            count = []
            while formula[i].isdigit():
                count.append(formula[i])
                i += 1
            return int(''.join(count)) if count else 1, i

        def f(i, d):
            while i < len(formula):
                if formula[i] == '(':
                    i, data = f(i + 1, defaultdict(int))
                    count, i = get_count(i)
                    for k, v in data.items():
                        d[k] += v * count
                elif formula[i] == ')':
                    return i + 1, d
                else:
                    atom = [formula[i]]
                    i += 1
                    while formula[i].islower():
                        atom.append(formula[i])
                        i += 1
                    count, i = get_count(i)
                    d[''.join(atom)] += count

        _, data = f(0, defaultdict(int))
        return ''.join(f'{atom}{count if count > 1 else ""}' for atom, count in sorted(data.items()))


print(Solution().countOfAtoms('K4(ON(SO3)2)2'))
