import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    patterns = []
    for _ in range(n):
        pattern = input().strip()
        patterns.append( pattern )

    answer_mask = []

    pattern_len = len(patterns[-1])
    for col in range(pattern_len):
        different_chr_set = set()
        for row in range(n):
            current_pattern_chr = patterns[row][col]
            if current_pattern_chr != '?':
                different_chr_set.add( current_pattern_chr )

        diff_cnt = len(different_chr_set)
        if diff_cnt == 0:
            answer_mask.append('x')
        elif diff_cnt == 1:
            only_chr_in_set = next(iter(different_chr_set))
            answer_mask.append(only_chr_in_set)
        else:
            answer_mask.append('?')

    print("".join(answer_mask))


if __name__ == "__main__":
    main()