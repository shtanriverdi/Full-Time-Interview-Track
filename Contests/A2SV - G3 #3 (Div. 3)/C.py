import sys
input = sys.stdin.readline

def main():
    a = [ *input().strip() ]
    b = [ *input().strip() ]

    a_len = len(a)
    b_len = len(b)
    max_a_b = max(a_len, b_len)

    a_str = "".join(a)
    b_str = "".join(b)

    if (a_str == b_str):
        print("-1")
    else:
        print(max_a_b)


if __name__ == "__main__":
    main()