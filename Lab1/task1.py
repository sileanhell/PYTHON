### Выведите сообщение-приветствие на экран, используя функцию print() и input(), запросив от пользователя его имя. Сохраните изменения в файле из созданной ранее папки. Интерпретируйте код и заметьте результат.
user_name = input("Введите ваше имя: ")
print("Привет, " + user_name + "! Добро пожаловать!")

### Определите 4 переменные, используя правильные названия для них в Python. Присвойте каждой из них, последовательно: числовое целое значение, вещественное значение, короткое текстовое значение, текстовое значение, которое занимает 3-4 строки.
integer_variable = 42
float_variable = 3.14
short_text_variable = "Привет!"
multiline_text_variable = """
Это многострочный текст.
Он может занимать несколько строк.
Пример использования переменной для хранения такого текста.
"""

### Выведите на экран тип данных для двух определенных ранее переменных.
print("Тип данных для integer_variable:", type(integer_variable))
print("Тип данных для float_variable:", type(float_variable))

### Для одной из определенных текстовых переменных, выведите длину текстовой строки.
print("Длина строки в multiline_text_variable:", len(multiline_text_variable))

### Преобразуйте текст, сохраненный в одну из текстовых переменных в буквах из верхнего регистра. Выведите результат на экран.
uppercase_text_variable = multiline_text_variable.upper()
print("Текст в верхнем регистре:\n", uppercase_text_variable)

### «Отрежьте», при помощи оператора [], а потом выведите подстроку из какой-то текстовой переменной.
substring = short_text_variable[1:4]
print("Отрезанная подстрока из short_text_variable:", substring)
