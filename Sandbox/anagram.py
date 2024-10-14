from collections import Counter
from time import time
import sys
a = "apple"
a1 = "paelp"
b = "nationalencyklopedi"
b1 = "nliciplyeakeonniotda"
c = "förskolepedagog"
c1 = "pfggokreöolasdl"

d = "qwyuifghqwuipfhqwfhqwpifhqwuipfhqwipfuhqwfuiphqwfuiphqwfipuhqwfiuhqwfipuhqwfipuhqwfuiphqwipfhuqwfipuhqwfuiphqwfupqwfpui"
dd = "qwyuifghqwuipfhqwfhqwpifhqwuipfhqwipfuhqwfuiphqwfuiphqwfipuhqwfiuhqwfipuhqwfipuhqwfuiphqwipfhuqwfipuhqwfuiphqwfupqwfpui"

def anagram(text, text1):
    if len(text) != len(text1):
        print("hejpådig")
        return False
    dic = dict()
    for char in text:
        if not char in dic:
            dic[char] = 1
        else:
            dic[char] = dic[char] + 1
    dic1 = dict()
    for char in text1:
        if char not in dic:
            return False
        if not char in dic1:
            dic1[char] = 1
        else:
            dic1[char] = dic1[char] + 1
    if dic == dic1:
        return True
    else:
        return False


def anagram_sort(text, text1):
    return sorted(text) == sorted(text1)




def anagram_counter(text, text1):
    return Counter(text) == Counter(text1)

print(sys.getsizeof(""))
exit()
start = time()
if anagram_counter(d, dd):
    print("wohoo")
else:
    print("neheee")
end = time()
print(end-start)

start = time()
if anagram_sort(d, dd):
    print("wohoo")
else:
    print("neheee")
end = time()
print(end-start)