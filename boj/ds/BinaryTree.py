from collections import deque

if __name__ == '__main__':

    # Binary Tree에 사용할 Node
    class Node(object):
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    # Binary Tree이 default Node로 root를 가진다.
    # level 0
    class BinaryTree(object):
        def __init__(self):
            self.root = None


    # Binary Tree를 순회하는 메소드
    def bfs(bt):
        if bt.root is None:
            return []

        visited = []
        queue = deque()
        queue.append(bt.root)

        # queue가 완전히 비어질 때 까지 반복문 실행
        while queue:
            # queue에 존재하는 노드를 dequeue하며 해당 노드의 value를 list에 담는다.
            # 반복문 안에 들어온다는 것은 queue에 노드가 반드시 존재한다.
            cur_node = queue.popleft()
            visited.append(cur_node.value)

            # 현재 Node에 자손이 존재하는 경우 queue에 enque
            # 현재 노드의 왼쪽 자손이 존재하면 enque해준다.
            if cur_node.left:
                queue.append(cur_node.left)

            # 현재 노드의 오른쪽 자손이 존재하면 enque해준다.
            if cur_node.right:
                queue.append(cur_node.right)

        return visited

    # level 0 : root Node
    bt = BinaryTree()
    bt.root = Node(0)

    # level 1 : root Node의 자손
    bt.root.left = Node(1)
    bt.root.right = Node(2)

    # level 2
    bt.root.left.left = Node(3)
    bt.root.left.right = Node(4)

    bt.root.right.left = Node(5)
    bt.root.right.right = Node(6)

    result = bfs(bt)
    print(result)