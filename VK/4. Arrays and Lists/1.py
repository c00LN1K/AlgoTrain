n = int(input())
lst = list(map(int, input().split()))
element = int(input())

print(len(lst) - lst.count(element))
