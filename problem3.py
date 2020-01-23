from collections import deque


def main():
    n, d = map(int, input().split())
    a = [int(x) for x in input().split()]
    a = deque(a)
    a.rotate(-d)
    print(*list(a))


if __name__ == "__main__":
    main()
    """
    5 4
    1 2 3 4 5
    """
