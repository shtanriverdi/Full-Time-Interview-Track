import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        walk_time, lift_between_time, lift_floor = list(map(int, input().split()))

        walk_to_lift_time = walk_time * lift_floor
        lift_come_time = 2 * (lift_between_time * lift_floor)
        A = min(walk_to_lift_time, lift_come_time)

        walk_to_4th_time = (4 - lift_floor) * walk_time
        lift_to_4th_time = (4 - lift_floor) * lift_between_time
        B = min(walk_to_4th_time, lift_to_4th_time)

        print(A + B)


if __name__ == "__main__":
    main()
