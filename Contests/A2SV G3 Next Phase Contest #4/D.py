import sys
input = sys.stdin.readline

def binarySearch(start_index, end_index, prefix_list, target):
    left = start_index
    right = end_index
    while left <= right:
        mid = left + (right - left) // 2
        if prefix_list[mid] == target:
            return mid
        elif prefix_list[mid] > target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    t = int(input())
    for _ in range(t):

        n = int(input())
        nums = list(map(int, input().split()))
        
        right_prefix = nums.copy()
        for i in range(1, n):
            right_prefix[i] += right_prefix[i - 1]
        
        left_prefix = nums.copy()
        for i in range(n - 2, -1, -1):
            left_prefix[i] += left_prefix[i + 1]

        x_candy_count = 0
        y_candy_count = 0
        best_answer = 0
        for i in range(n):
            found = binarySearch(i + 1, n - 1, left_prefix, right_prefix[i])
            if found != -1:
                x_candy_count = i + 1
                y_candy_count = n - found
                possible_answer = x_candy_count + y_candy_count
                best_answer = max(possible_answer, best_answer)
        
        print(best_answer)
        

if __name__ == "__main__":
    main()