def clear_string(s: str):
    current_s = []
    cursor_index = 0
    for k, v in {'<delete>': '4', '<bspace>': '3', '<left>': '1', '<right>': '2'}.items():
        s = s.replace(k, v)
    for i in range(len(s)):
        if s[i].isalpha():
            current_s.insert(cursor_index, s[i])
            cursor_index += 1
        elif s[i] == '1':
            cursor_index = max(0, cursor_index - 1)
        elif s[i] == '2':
            cursor_index = min(cursor_index + 1, len(current_s))
        elif s[i] == '3':
            if cursor_index != 0:
                current_s.pop(cursor_index - 1)
                cursor_index = max(0, cursor_index - 1)
        else:
            if cursor_index != len(current_s):
                current_s.pop(cursor_index)
    return ''.join(current_s)


task = input().strip()
answer = input().strip()
print('Yes' if task == clear_string(answer) else 'No')
