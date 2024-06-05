a = '''hi, I am 
surbhi, 
ABC, 
RFDEDDF, 
DFDGG 
'''

word_count = {}

words = a.split()
print(words)

for word in words:
   word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"'{word}' occurs {count} times.")

