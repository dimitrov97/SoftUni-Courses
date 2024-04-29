from collections import deque

water = int(input())
name = input()
peoples_queue = deque()

while name != "Start":

    peoples_queue.append(name)
    name = input()


command = input()
while command != "End":

    if " " in command:
        command = command.split()
        water += int(command[1])
    else:
        removed_person = peoples_queue.popleft()
        if water >= int(command):
            water -= int(command)
            print(f"{removed_person} got water")
        else:
            print(f"{removed_person} must wait")

    command = input()
print(f"{water} liters left")
