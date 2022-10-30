def max_vizitors_line(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))
    events.sort()
    online = 0
    max_online = 0
    for event in events:
        if event[1] == -1:
            online += 1
        else:
            online -= 1
        max_online = max(online, max_online)
    return max_online


n = int(input())
tin = list(map(int, input().split()))
tout = list(map(int, input().split()))
print(max_vizitors_line(n, tin, tout))