
n = int(input("Умова 1<n<9. Введіть кількість рядків n: "))

while(n <= 1 or n >= 9):
    print("Введене число не задовольняє умові")
    n = int(input("Введіть ще раз n: "))

for i in range(1, n + 1):
    for j in range(i, n + 1):
        print(j, end=" ")
    print("")
 
