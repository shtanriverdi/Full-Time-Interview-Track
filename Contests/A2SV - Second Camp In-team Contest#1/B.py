import sys
from collections import defaultdict 
input = sys.stdin.readline

def main():
    word = [ *input().strip() ]
    n = len(word)

    letters_map = defaultdict(list)
    for i in range(27):
        letters_map[i] = [-1, -1]

    for index, letter in enumerate(word):
        letter_key = ord(letter) - 97
        prev_index, max_diff = letters_map[letter_key]
        new_diff = abs(index - prev_index)
        letters_map[letter_key][1] = max(max_diff, new_diff)
        letters_map[letter_key][0] = index

    # Compare with lenghts
    for key in letters_map.keys():
        prev_index, max_diff = letters_map[key]
        new_diff = abs(n - prev_index)
        letters_map[key][1] = max(max_diff, new_diff)

    answer = float("inf")
    for index, diff in letters_map.values():
        if index != -1:
            answer = min(answer, diff)

    print(answer)

if __name__ == "__main__":
    main()
