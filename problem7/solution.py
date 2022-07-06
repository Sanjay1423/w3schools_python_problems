word = input()
word_list = sorted(list(word))
dict = {}
for i in word:
    dict[ord(i)] = i

for i in word_list:
    print(dict[ord(i)], end='')
