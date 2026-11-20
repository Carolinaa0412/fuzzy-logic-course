import math

# загальна трикутна функція належності
def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    if x == b:
        return 1.0
    if x < b:
        return (x - a) / (b - a)
    return (c - x) / (c - b)

# функції належності для температури
def temp_low(x):
    return triangular(x, 0, 0, 20)

def temp_medium(x):
    return triangular(x, 10, 20, 30)

def temp_high(x):
    return triangular(x, 20, 40, 40)

# функції належності для швидкості вентилятора
def fan_low(x):
    return triangular(x, 0, 0, 50)

def fan_medium(x):
    return triangular(x, 25, 50, 75)

def fan_high(x):
    return triangular(x, 50, 100, 100)

# введення даних
temp_input = float(input("Введіть температуру повітря (°C): "))

if temp_input < 0 or temp_input > 40:
    print("Помилка: температура має бути в діапазоні від 0 до 40 °C.")
    exit()

# фізифікація
deg_low = temp_low(temp_input)
deg_med = temp_medium(temp_input)
deg_high = temp_high(temp_input)

print("\n Результати фазифікації")
print(f"Низька: {deg_low:.3f}")
print(f"Середня: {deg_med:.3f}")
print(f"Висока: {deg_high:.3f}")

# правила Мамдані
# правило 1 - Якщо Temp=Низька -> Speed=Низька
rule1_activation = deg_low

# правило 2 - Якщо Temp=Середня -> Speed=Середня
rule2_activation = deg_med

# правило 3 - Якщо Temp=Висока -> Speed=Висока
rule3_activation = deg_high

print("\n Ступені активації правил")
print(f"Правило 1 (Fan Low): {rule1_activation:.3f}")
print(f"Правило 2 (Fan Medium): {rule2_activation:.3f}")
print(f"Правило 3 (Fan High): {rule3_activation:.3f}")

step = 1
aggregated_output = []

for speed in range(0, 101, step):
    # обрізання оператором min
    v_low = min(rule1_activation, fan_low(speed))
    v_med = min(rule2_activation, fan_medium(speed))
    v_high = min(rule3_activation, fan_high(speed))
    
    # aгрегування оператором max
    aggregated_val = max(v_low, v_med, v_high)
    aggregated_output.append((speed, aggregated_val))

# mетод центра ваги
numerator = sum(speed * degree for speed, degree in aggregated_output)
denominator = sum(degree for speed, degree in aggregated_output)

if denominator == 0:
    final_speed = 0.0
else:
    final_speed = numerator / denominator

print("\n Підсумковий результат")
print(f"Рекомендована швидкість вентилятора: {final_speed:.2f}%")