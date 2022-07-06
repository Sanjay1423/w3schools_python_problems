number = input()
number_list = []
for i in number:
    number_list.append(int(i))
print(f'The Largest digit of the said number: {max(number_list)}')
print(f'The Smallest digit of the said number: {min(number_list)}')
