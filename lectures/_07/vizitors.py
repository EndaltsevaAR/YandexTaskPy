def one_vizitors_line(n, tin, tout):
    events = []
    for i in range(n):
        events.append((tin[i], -1))
        events.append((tout[i], 1))
    events.sort()
    online = 0
    time = 0
    for i in range(len(events)):
        if online > 0:
            time += events[i][0] - events[i-1][0]
        if events[i][1] == -1:
            online += 1
        else:
            online -= 1
    return time


n = int(input())
tin = list(map(int, input().split()))
tout = list(map(int, input().split()))
print(one_vizitors_line(n, tin, tout))
