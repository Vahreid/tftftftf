# решение задачи

money = [1,2,4,8,16,32,64]

n = int(input('введите нужную вам сумму: '))

bills = []
n1 = 0
i = -1

while n1 != n:
    if n1 + money[i] > n:
        i -= 1
    else:
        n1 += money[i]
        bills.append(money[i])

print(bills)