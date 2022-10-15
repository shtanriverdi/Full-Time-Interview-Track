import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    pokemons = [ *input().strip() ]

    poke_set = set()
    for poke in pokemons:
        poke_set.add(poke)

    all_pokes_count = len(poke_set)

    window_map = defaultdict(int)

    left = 0
    right = 0
    answer = n

    while right < n:
        window_map[ pokemons[right] ] += 1

        while len(window_map) == all_pokes_count:
            answer = min(answer, right - left + 1)
            window_map[ pokemons[left] ] -= 1
            if window_map[ pokemons[left] ] == 0:
                window_map.pop( pokemons[left] )
            left += 1

        right += 1

    print(answer)
        

if __name__ == "__main__":
    main()