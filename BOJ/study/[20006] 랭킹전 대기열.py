import sys
input = sys.stdin.readline

p, m = map(int, input().split())

rooms = []
for _ in range(p):
    l, n = input().strip().split()
    l = int(l)
    
    room_index = -1
    for i in range(len(rooms)):
        if rooms[i][0][1]-10 <= l <= rooms[i][0][1]+10 and len(rooms[i]) < m:
            room_index = i
            break
    if room_index == -1:
        rooms.append([[n, l]])
    else:
        rooms[room_index].append([n, l])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    
    room.sort()
    for person in room:
        n, l = person
        print(f'{l} {n}')
