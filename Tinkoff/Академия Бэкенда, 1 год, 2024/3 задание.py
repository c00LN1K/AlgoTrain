n, k, a, m = map(int, input().split())
curr = 0
moves = 0


class Generator:
    seed = 0

    @staticmethod
    def lcg(e):
        return (a * e + 11) % m

    @classmethod
    def generator(cls):
        cls.seed = cls.lcg(cls.seed)
        val = (abs(cls.seed % 3 - 1) * 5 + abs(cls.seed % 3) * 2) % 8
        return val


while n > 0:
    while curr < 3 * k:
        curr += Generator.generator()
        moves += 1
    n -= curr // 3
    curr %= 3

print(moves)
