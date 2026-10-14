# Exercise 19. Anagram Detector

def check_anagram(s1, s2):

    return sorted(s1.lower()) == sorted(s2.lower())

s1 = "listen"
s2 = "silent"

if check_anagram(s1, s2):
    print(f"{s1} and {s2} are anagrams.")
else :
    print(f"{s1} and {s2} are NOT anagrams.")

