import sys
from collections import defaultdict
input = sys.stdin.readline

def binarySearch(key, nums, n):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if key < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return right

def main():
    t = int(input())
    for _ in range(t):

        height_count, question_count = list(map(int, input().split()))
        height_count += 1

        heights = [0] + list(map(int, input().split()))
        questions = list(map(int, input().split()))

        for i in range(1, height_count):
            heights[i] += heights[i - 1]

        max_diff_so_far = 0
        max_diff_needed = [ 0 ]
        for i in range(1, height_count):
            cur_diff = heights[i] - heights[i - 1]
            if cur_diff > max_diff_so_far:
                max_diff_so_far = cur_diff

            max_diff_needed.append(max_diff_so_far)

        answers = []
        for question in questions:
            right_most_index = binarySearch(question, max_diff_needed, height_count)
            answers.append(heights[right_most_index])
        
        for answer in answers:
            print(answer, "", end="")
        print()

if __name__ == "__main__":
    main()