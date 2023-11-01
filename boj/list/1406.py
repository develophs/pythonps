from sys import stdin

if __name__ == '__main__':
    class Node(object):
        def __init__(self, val="", next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev

    class Editor(object):
        def __init__(self, default):
            cursor = Node()
            self.head = self.current = cursor

            for i in default:
                if self.current.prev is None:
                    new_node = Node(val=i, next=self.current)
                    self.current.prev = new_node
                else:
                    new_node = Node(val=i, next=self.current, prev=self.current.prev)
                    self.current.prev.next = new_node
                    self.current.prev = new_node

        def P(self, text):
            new_node = Node(val=text, next=self.current, prev=self.current.prev)
            self.current.prev.next = new_node
            self.current.prev = new_node

        def L(self):
            if self.current.prev:
                new_node = Node(next=self.current.prev, prev=self.current.prev.prev)
                self.current.prev.prev.next = new_node
                self.current.prev.prev = new_node
                self.current.prev.next = None # 기존 cursor 삭제

        def D(self):
            if self.current.next:
                new_node = Node(prev=self.current.next)
                self.current.next.next = new_node
                self.current.next.prev = self.current.prev
                self.current.prev.next = self.current.next

        def B(self):
            if self.current.prev:
                self.current.prev.prev.next = self.current
                self.current.prev = self.current.prev.prev

        def getText(self):
            text = ""
            current_node = self.head.next
            while current_node:
                text += current_node.val
                current_node = current_node.next
            return text

    default = stdin.readline().strip()
    editor = Editor(default)

    step = int(stdin.readline())

    while step > 0:
        line = stdin.readline().split()

        if line[0] == "L":
            editor.L()
        elif line[0] == "D":
            editor.D()
        elif line[0] == "B":
            editor.B()
        elif line[0] == "P":
            editor.P(line[1])
        step -= 1

    result_text = editor.getText()
    print(result_text)