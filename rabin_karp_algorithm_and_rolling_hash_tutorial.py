# String Hashing by using Rabin Karp Algorithm

# 1) Calculation of the hash of a string
# Simple function that calculates hash value of a string by using polynomial rolling hash
def main():
    hash_value = compute_hash("abc")
    print("Hash of abc:", hash_value) # 2946

# Calculating the hash of a string which contains only lowercase letters
def compute_hash(s):
    p = 31
    m = 1e9 + 9
    hash_value = 0
    pow_value = 1
    for c in s:
        value = ord(c) - ord('a') + 1
        hash_value += (value * pow_value) % m
        pow_value = (p * pow_value) % m
    return hash_value

if __name__ == "__main__":
    main()
