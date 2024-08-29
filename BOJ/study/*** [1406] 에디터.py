import sys
input = sys.stdin.readline

# Linked List와 같이 노드 간의 이동, 삽입, 삭제가 빈번한 경우
# dict로 구현하면 안되며, class로 구현하기

class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.cursor = self.head

    def insert(self, data):
        new_node = Node(data)

        new_node.prev = self.cursor
        new_node.next = self.cursor.next

        if self.cursor.next:
            self.cursor.next.prev = new_node
        self.cursor.next = new_node

        self.cursor = new_node

    def move_left(self):
        if self.cursor.prev:
            self.cursor = self.cursor.prev

    def move_right(self):
        if self.cursor.next:
            self.cursor = self.cursor.next

    def delete(self):
        if self.cursor != self.head:
            self.cursor.prev.next = self.cursor.next
            if self.cursor.next:
                self.cursor.next.prev = self.cursor.prev
            self.cursor = self.cursor.prev

    def get_result(self):
        result = []
        node = self.head.next
        while node:
            result.append(node.data)
            node = node.next
        return ''.join(result)

string = list(input().rstrip())
M = int(input())

ll = LinkedList()
for s in string:
    ll.insert(s)

for _ in range(M):
    command = input().split()

    if command[0] == 'L':
        ll.move_left()
    
    elif command[0] == 'D':
        ll.move_right()
    
    elif command[0] == 'B':
        ll.delete()
    
    elif command[0] == 'P':
        ll.insert(command[1])

print(ll.get_result())