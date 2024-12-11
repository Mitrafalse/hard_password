def generate_password(n):
    result = ""
    pairs = []

    # Генерируем уникальные пары от 1 до 20
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pairs.append((i, j))

    # Проверяем делимость `n` на сумму каждой пары и формируем пароль
    for pair in pairs:
        sum_of_pair = sum(pair)
        if n % sum_of_pair == 0:
            result += f"{pair[0]}{pair[1]}"

    return result

# Пример использования функции:
number = int(input("Введите число от 3 до 20: "))
if 3 <= number <= 20:
    password = generate_password(number)
    print("Ваш пароль:", password)
else:
    print("Число вне диапазона!")