from collections import deque

peoples = input()
peoples_deque = deque()

while peoples != "End":
    if peoples == "Paid":
        while peoples_deque:
            served_customer = peoples_deque.popleft()
            print(served_customer)
    else:
        peoples_deque.append(peoples)

    peoples = input()
print(f"{len(peoples_deque)} people remaining.")
