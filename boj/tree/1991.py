from sys import stdin

if __name__ == '__main__':
    # 재귀를 사용하여 자손에게 위임하고 자손에 연결된 노드들 부터 먼저 방문한다.
    # 일반적인 트리 순회의 사간복잡도 O(n)
    # 트리의 접근하는 순서는 항상 같다.! 값을 처리하는 순서가 달라지는것이다!!

    # 전위 순회 : 자손노드에 방문하기 전 부모 노드부터 방문하여 값을 처리한다.
    def pre_order(cur_value):
        if cur_value != ".":
            print(cur_value, end="")
            pre_order(tree[cur_value][0])
            pre_order(tree[cur_value][1])

    # 중위 순회 : 한쪽 방향의 자손, 노드들을 방문 한 후 본인의 노드를 방문하여 값을 처리한다.
    def in_order(cur_value):
        if cur_value != ".":
            in_order(tree[cur_value][0])
            print(cur_value, end="")
            in_order(tree[cur_value][1])

    # 후위 순회 : 양방향 자손 노드, 서브트리를 방문하여 값을 처리하고 본인의 노드를 방문하여 처리한다.
    def post_order(cur_value):
        if cur_value != ".":
            post_order(tree[cur_value][0])
            post_order(tree[cur_value][1])
            print(cur_value, end="")

    n = int(stdin.readline().rstrip())

    # 트리를 구성하기 위해 딕셔너리를 사용
    # 노드를 사용했었지만, 입력값을 받아 노드로 구성하기 너무 힘들다.
    tree = {}

    for _ in range(n):
        value, left, right = stdin.readline().rstrip().split()
        tree[value] = [left, right]

    pre_order("A")
    print()
    in_order("A")
    print()
    post_order("A")