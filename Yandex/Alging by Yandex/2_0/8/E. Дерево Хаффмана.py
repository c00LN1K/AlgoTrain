def read_tree(tree, stack):
    global index
    if index >= len(tree):
        ans.append(''.join(stack))
        return
    el = tree[index]
    index += 1
    if el == 'D':
        read_tree(tree, stack + ['0'])
    else:
        if stack:
            ans.append(''.join(stack))
        while stack and stack[-1] == '1':
            stack.pop()
        if stack:
            stack[-1] = '1'
        else:
            stack.append('1')
        read_tree(tree, stack)


n = int(input())
for i in range(n):
    tree = input()
    index = 0
    ans = []
    read_tree(tree, [])
    print(len(ans))
    print(*ans, sep='\n')

# DDUUDUDU
