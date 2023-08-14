if __name__ == '__main__':
    my_list = list(map(int, input().split()))
    my_list.sort()
    for i in my_list:
        print(i, end=" ")
