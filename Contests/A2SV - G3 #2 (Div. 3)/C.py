import sys
import heapq
input = sys.stdin.readline

def clear_the_word(word):
    clean_word = []
    for letter in word:
        if letter != '*':
            clean_word.append(letter)
    return clean_word

def main():
    t = int(input())
    for _ in range(t):
        word = [ *input().strip() ]
        p = int(input())

        current_price = 0
        weight_index_list = []
        for index, letter in enumerate(word):
            letter_weight = ord(letter) - ord('a') + 1
            current_price += letter_weight
            weight_index_list.append([letter_weight, index])
            
        max_heap = []
        for weight, index in weight_index_list:
            heapq.heappush(max_heap, [weight * -1, index])
        
        while max_heap and current_price > p:
            weight, index = heapq.heappop(max_heap)
            current_price -= (weight * -1)
            word[index] = '*'

        clean_word = clear_the_word(word)
        print(''.join(clean_word))

if __name__ == "__main__":
    main()