import sys
input = sys.stdin.readline

def main():
    n = int(input())
    word = [ *input().strip() ]

    i = 1
    while i < n:
        if word[i] != word[i - 1]:
            word[i] = '*'
            word[i - 1] = '*'
            i +=1
        i += 1

    count = [ [1, word[0]] ]
    for i in range(1, n):
        if word[i] == count[-1][1]:
            count[-1][0] += 1
        else:
            count.append([1, word[i]])

    max_star_count = 0
    for pair in count:
        if pair[1] == '*':
            max_star_count = max(max_star_count, pair[0])

    print(max_star_count)

if __name__ == "__main__":
    main()