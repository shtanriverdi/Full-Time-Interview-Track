class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_set = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' }
        
        vowels = []
        for index, letter in enumerate(s):
            if letter in vowel_set:
                vowels.append([letter, index])
        
        vowels_len = len(vowels)
        for i in range(vowels_len // 2):
            vowels[i][0], vowels[vowels_len - i - 1][0] = vowels[vowels_len - i - 1][0], vowels[i][0]
            
        s_list = list(s)
        for vowel, index in vowels:
            s_list[index] = vowel
            
        return "".join(s_list)