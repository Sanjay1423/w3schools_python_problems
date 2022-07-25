# Replace all 'P' with '9', 'T' with '0', 'S' with '1', 'H' with '6' and 'A' with '8'

dict = {'P': 9, 'T': 0, 'S': 1, 'H': 6, 'A': 8}

string_1 = input().upper()
lst = []
for i in string_1:
    if i in dict:
        lst.append(str(dict[i]))
    else:
        lst.append(i)

print(''.join(lst))
