from collections import deque

names = deque(input().split())
n_toss = int(input()) - 1

while len(names) > 1:
    for _ in range(n_toss):
        removed_person = names.popleft()
        names.append(removed_person)
    print(f"Removed {names.popleft()}")

print(f"Last is {''.join(names)}")
