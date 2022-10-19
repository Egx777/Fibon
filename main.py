def Fibon(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibon(n-2) + Fibon(n-1)
n = int(input("Введите число"))
print(Fibon(n))