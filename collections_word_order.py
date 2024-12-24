
#input
n=int(input()) # number of words
items=[input().strip() for _ in range(n)] #list of words

#process
unique_words=[]
counts=[]

for word in items:
    if word not in unique_words:
        unique_words.append(word)
        counts.append(items.count(word))

#output
print(len(unique_words))
print(' '.join(map(str,counts)))
      
