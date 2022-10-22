# sorting lists (mutable objects)
def sort(seq):
    min_val = min(seq)
    max_val = max(seq)
    k = max_val - min_val + 1
    count = [0] * k
    for current in seq:
        count[current - min_val] += 1
    count_position = 0
    for value in range(0, k):
        for i in range(count[value]):
            seq[count_position] = value + min_val
            count_position += 1
    return seq


sequn = list(map(int, input().split()))
print(sort(sequn))
