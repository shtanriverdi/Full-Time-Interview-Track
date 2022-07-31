import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = str(input())
        digits = []
        for i in range(len(n)-1):
            digits.append(int(n[i]))
        
        even_found = False
        for digit in digits:
            if digit % 2 == 0:
                even_found = True
                break

        last_digit = digits[-1]
        first_digit = digits[0]
        
        # No even at all
        if even_found == False:
            print("-1")
        # Last digit is even
        elif last_digit % 2 == 0:
            print("0")
        # First digit is even
        elif first_digit % 2 == 0:
            print("1")
        else:
            print("2")


if __name__ == "__main__":
    main()