import sys
input = sys.stdin.readline

def count(zipped):
    even_count = 0
    odd_count = 0
    for item in zipped:
        if item == 'E':
            even_count += 1
        else:
            odd_count += 1
    return [even_count, odd_count]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))

        even_odd_list = []
        for num in nums:
            # Even
            if num % 2 == 0:
                even_odd_list.append('E')
            # Odd
            else:
                even_odd_list.append('O')
                
        even_count, odd_count = count(even_odd_list)
        print(min(even_count, odd_count))


if __name__ == "__main__":
    main()