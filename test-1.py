a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

while b == 0:
    print("Ноль нельзя.")
    break
else: print(a / b)

a = 10
b = 0

result = {
    True: lambda: "Деление на ноль нельзя",
    False: lambda: a / b
}[b == 0]()

print(result)

result = (b != 0 and a / b) or "Нельзя делить на ноль"
print(result)