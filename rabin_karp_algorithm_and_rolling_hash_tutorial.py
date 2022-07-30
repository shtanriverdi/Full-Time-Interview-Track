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

    
    
# --------- Rabin Karp Algorithm ------------
# Problem: Given two strings s -> "pattern" and t -> "text", 
# determine if the pattern appears in the text and if it does
# enumerate all its occurrences in O(M + N)  time.
def main():
    s = "ll"
    t = "hello"
    occurences = rabin_karp(s, t)
    print("All Occurences: ", occurences)
    
# Rabin-Karp Algorithm for string matching
def rabin_karp(s, t):
    size_S = len(s)
    size_T = len(t)
    
    occurrences = []
    if size_T < size_S or size_S == 0 or size_T == 0:
        return occurrences
    
    # Prime Values to avoid collision
    p = 31
    m = 1e9 + 9
    
    # Calculate hash value for pattern string "s" and "t"
    hash_value_S = 0
    hash_value_window_T = 0
    base = 1
    for i in range(size_S):
        # Calculating hash value for pattern "s"
        letter_value_S = ord(s[i]) - ord('a') + 1
        hash_value_S += (letter_value_S * base) % m
        # Calculating hash value for text "t"
        letter_value_T = ord(t[i]) - ord('a') + 1
        hash_value_window_T += (letter_value_T * base) % m
        # Update base: p^0 -> p^1
        base = (base * p) % m
    
    # Calculate the power value to be used for the element be deleted
    # a b c = (1 * p^2) + (2 * p^1) + (3 * p^0)
    # power_value = p^n-1 where n is the lenght of the pattern string
    # This will be the greatest power value, the left most one
    power_value = 1
    for _ in range(size_S - 1):
        power_value = (power_value * p) % m
    
    # Check the first window
    if hash_value_window_T == hash_value_S:
        occurrences.append(0)
    
    # Roll the hash, slide the window and update window's hash value
    # by checking whether the hashes are equal or not
    # 0 1 2 3 4
    # a b c     -> pattern
    # a b c d e -> string
    #   ^---^
    #   L   R
    for right_pointer in range(size_S, size_T):
        # Remove the left most letter from hash_value
        left_pointer = right_pointer - size_S
        left_letter_value = ord(t[left_pointer]) - ord('a') + 1
        # Update window hash value
        hash_value_window_T -= (left_letter_value * power_value)
        
        # Add the right letter to hash_value
        right_letter_value = ord(t[right_pointer]) - ord('a') + 1
        # Update the window hash value by shifting to left
        hash_value_window_T = (hash_value_window_T * p) % m
        hash_value_window_T += right_letter_value
        
        # Avoid negative window hash value
        hash_value_window_T += m
        
        print(hash_value_S)
        print(hash_value_window_T)
        
        # Check is hashes are equal meaning that we found a match
        if hash_value_window_T == hash_value_S:
            occurrences.append(left_pointer + 1)
        
    return occurrences

if __name__ == "__main__":
    main()
