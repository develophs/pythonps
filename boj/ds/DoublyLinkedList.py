if __name__ == '__main__':
    class Node(object):

        def __init__(self, val="", next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev


    # 클래스의 파라미터는 object로 지정하고,
    # 생성자 (__init__)의 파라미터를 성정한다.
    # self는 객체 자기 자신을 가리킨다. self를 그냥 사용하면 객체가 나옴
    # 객체의 프로퍼티를 사용하기 위해서는 self.프로퍼티한다.
    class BrowserHistory(object):

        def __init__(self, homepage):
            self.head = self.current = Node(val=homepage)

        def visit(self, url):
            new_node = Node(val=url, prev=self.current)

            self.current.next = new_node
            self.current = self.current.next

            return None

        def back(self, steps):
            while steps > 0 and self.current.prev:
                self.current = self.current.prev
                steps -= 1

            return self.current.val

        def forward(self, steps):
            while steps > 0 and self.current.next:
                self.current = self.current.next
                steps -= 1

            return self.current.val

    bh = BrowserHistory("leetcode.com")
    bh.visit("google.com")
    bh.visit("facebook.com")
    bh.visit("youtube.com")

    prev = bh.back(1)
    print(prev)

    next = bh.forward(1)
    print(next)

    the_last = bh.forward(5000)
    print(the_last)
