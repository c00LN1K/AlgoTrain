class Solution:
    def fractionAddition(self, expression: str) -> str:
        last_numerator = 0
        last_denominator = 1
        lst = expression.replace('-', '+-').split('+')
        for number in lst:
            if not number:
                continue
            numerator, denominator = map(int, number.split('/'))
            if max(denominator, last_denominator) % min(denominator, last_denominator) == 0:
                common_denominator = max(denominator, last_denominator)
            else:
                common_denominator = denominator * last_denominator
            last_numerator = last_numerator * common_denominator // last_denominator + numerator * common_denominator // denominator
            last_denominator = common_denominator
            print(f'{last_numerator}/{last_denominator}')
        return f'{last_numerator}/{last_denominator}'


print(Solution().fractionAddition("-1/2+1/2+1/3"))