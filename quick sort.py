from collections import deque
def simulate_kitchen(ops):
    orders = deque()
    list = []
    for i in range(0, len(ops)):
        if ops[i] == 'E':
            orders.append(ops[i+1])
        elif ops[i] == 'D':
            list.append(orders.popleft())
    return list
ops = input().split()
result = simulate_kitchen(ops)
print(*result)