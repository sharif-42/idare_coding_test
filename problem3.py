from collections import deque
n, d = map(int, input().split())

test_list = [int(x) for x in input().split()]
test_list = deque(test_list)
test_list.rotate(-2)
test_list = list(test_list)
print(test_list)

"""
5 4
1 2 3 4 5
"""