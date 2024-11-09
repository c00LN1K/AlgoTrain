num = int(input())
nums = list(map(int, input().split()))
total_sum = 0
for i in nums:
    total_sum ^= i

condition = all(pile == 1 for pile in nums)

if condition:
    print('Alice')
elif num == 1:
    print("Alice" if nums[0] % 2 == 1 else "Dmitry")
else:
    print("Alice" if total_sum != 0 else "Dmitry")
