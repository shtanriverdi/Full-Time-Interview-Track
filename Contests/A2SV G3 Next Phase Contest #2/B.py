import sys
input = sys.stdin.readline

def main():
    n = int(input())
    cen_x, cen_y = list(map(int, input().split()))
    ax, ay = list(map(int, input().split()))
    bx, by = list(map(int, input().split()))

    if ax < cen_x and bx < cen_x:
        if ay < cen_y and by < cen_y:
            print("YES")
        elif ay > cen_y and by > cen_y:
            print("YES")
        else:
            print("NO")

    elif ax > cen_x and bx > cen_x:
        if ay < cen_y and by < cen_y:
            print("YES")
        elif ay > cen_y and by > cen_y:
            print("YES")
        else:
            print("NO")
            
    else:
            print("NO")

if __name__ == "__main__":
    main()