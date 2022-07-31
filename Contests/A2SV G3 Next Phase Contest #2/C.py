import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        length, desired_sum = list(map(int, input().split()))
        nums = list(map(int, input().split()))

        zipped = [-1]
        for i, num in enumerate(nums):
            if num == 1:
                zipped.append(i)
        zipped.append(length)

        actual_sum = len(zipped) - 2
        if actual_sum < desired_sum:
            print("-1")

        elif actual_sum == desired_sum:
            print("0")

        else:
            answer = float("inf")
            left = 1
            right = desired_sum
            while right <= (len(zipped) - 2):
                left_part = zipped[left - 1] + 1
                right_part = length - zipped[right + 1]
                
                possible_answer = left_part + right_part
                answer = min(answer, possible_answer)
                
                right += 1
                left += 1

            print(answer)


if __name__ == "__main__":
    main()