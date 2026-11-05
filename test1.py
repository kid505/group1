# def is_valid(s):
#     stack = []
#     pairs = {')': '(', ']': '[', '}': '{'}
#     for ch in s:
#         if ch in '([{':
#             stack.append(ch)
#         else:
#             if not stack or stack[-1] != pairs[ch]:
#                 return False
#             stack.pop()
#     return not stack

# print(is_valid("(aa[{}]f)"))  
#from collections import deque


# def simulate_kitchen(ops):
#     queue = deque()
#     served = []

#     i = 0
#     while i < len(ops):
#         token = ops[i]
#         if token == "E":
#             queue.append(ops[i + 1])
#             i += 2
#         elif token == "D":
#             served.append(queue.popleft())
#             i += 1
#         else:
#             i += 1

#     return served
def simulate_undo(ops):
    stack = []
    i = 0
    while i < len(ops):
        token = ops[i]
        if token == "TYPE":
            stack.append(ops[i + 1])
            i += 2
        elif token == "UNDO":
            if stack:
                stack.pop()
            i += 1
        else:
            i += 1

    return stack

ops = input().split()
print(*simulate_undo(ops))