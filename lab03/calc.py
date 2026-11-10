def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Деление на ноль невозможно"
    return a / b

a = float(input("Первое число: "))
b = float(input("Второе число: "))

print("Сумма:", add(a, b))
print("Разность", subtract(a, b))
print("Произведение", multiply(a, b))
print("Частное", divide(a, b))
