import sys
input = sys.stdin.readline

def main():

    n, idle = list(map(int, input().split()))
    min_time = float("inf")
    entities = []
    for _ in range(n):
        Id, amount, time = list(map(int, input().split()))
        entities.append( [time, Id, amount] )
        min_time = min(min_time, time)

    end_time = min_time + idle
    max_amount = float("-inf")
    valids = []
    for (time, Id, amount) in entities:
        if time < end_time:
            valids.append( [Id, amount] )
            # Find max amount in valid entities
            max_amount = max(max_amount, amount)

    # Find max ID
    max_ID = float("-inf")
    for (Id, amount) in valids:
        if amount == max_amount:
            max_ID = max(max_ID, Id)

    print(max_ID)


if __name__ == "__main__":
    main()
