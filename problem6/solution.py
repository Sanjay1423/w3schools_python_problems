numbers = list(input().split(','))
check_list = []
sum = 0

for i in numbers:
    sum += 1
    if i not in check_list:
        check_list.append(i)
        if sum == len(numbers):
            print(True)
            break
    elif i in check_list:
        print(False)
        break
