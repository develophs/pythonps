if __name__ == '__main__':
    class Node:
        def __init__(self, value=0, next=None):
            self.value = value
            self.next = next

    class LinkedList(object):
        def __init__(self):
            self.head = None
            self.tail = None

        # 맨뒤의 node가 new_node를 가리켜야한다.
        # append의 시간 복잡도 O(n)
        def append(self, value):
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while (current.next):
                    current = current.next
                current.next = new_node

        #ArrayList은 O(1)이지만, LinkedList는 해당 인덱스에 대한 접근은 O(n)이다.
        def get(self, idx):
            current = self.head
            for i in range(idx):
                current = current.next
            return current.value

        # idx에 존재하는 Node를 참조하는 데이터가 존재하지 않으면 GC가 해당 Node를 제거한다.
        def remove(self, idx):
            current = self.head
            for i in range(idx-1):
                current = current.next
            current.next = current.next.next

        def insert_at(self, value, idx):
            current = self.head
            new_node = Node(value)

            for i in range(idx-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        #tail_append는 시간복잡도가 O(1)이지만, LinkedList 생성 시 head와 같이 초기화시켜준다.
        #self.head = None self.tail = None
        def tail_append(self, value):
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else :
                self.tail.next = new_node
                self.tail = self.tail.next

    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(7)

    llt = LinkedList()
    llt.tail_append(5)
    llt.tail_append(6)
    llt.tail_append(7)