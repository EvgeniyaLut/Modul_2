new_mail = 0

# Создадим собственную функцию и дадим ей имя check_mail ("проверка писем")
# В эту функцию поместим код проверки количества писем.
def check_mail():
    if new_mail > 0:
        print('Пришло письмо, не пропусти!')
    else:
        print('Никто не пишет.')

# Тут код, отсчитывающий минуту

# Проверим почту - вызовем функцию check_mail():
# запустим код, который хранится в функции.
check_mail()

# Тут код, отсчитывающий минуту

# И снова вызовем функцию:
check_mail()

# Тут код, отсчитывающий минуту
# За это время пришло письмо:
new_mail = 1

# И снова вызовем функцию:
check_mail()



# Объявление функции hello()
def hello():
    # А здесь началось тело функции
    print('Приветствую тебя, джедай Питона!')


def hello():
    print('Приветствую тебя, джедай Питона!')

# Раскомментируйте вызов функции hello():
# уберите символ # и пробел в начале следующей строки
hello()


# Объявление функции с параметром name
def hello(name):
    # Параметр name можно обрабатывать в теле функции:
    print(name + ', приветствую тебя!')

# Вызов функции с аргументом 'Максим'
hello('Максим')
# Будет напечатано: Максим, приветствую тебя!

# Раскомментируйте строку ниже, в качестве аргумента подставьте своё имя -
# и снова выполните код.
# hello('Имя')


# Теперь у функции hello() два параметра: name и bonus
def hello(name, bonus):
    # Оба параметра применим в теле функции:
    print(name + ', приветствую тебя! Бери ' + bonus)


hello('Дарт Вейдер', 'печеньки')

# И ещё раз вызовем, с другими аргументами:
hello('Винни Пух', 'мёд')

# Раскомментируйте вызов функции, подставьте в него аргументы
# и вновь запустите код
# hello('Имя', 'что-то вкусное')


def hello(name):
    print('Привет, ' + name)


students = ['Ира', 'Маша', 'Ваня', 'Петя']

for student in students:
    hello(student)

# А можно и наоборот: переписать эту программу так, чтобы цикл был внутри тела функции:

students = ['Ира', 'Маша', 'Ваня', 'Петя']

def hello():
    for student in students:
          print('Привет, ' + student)

hello()



# Код функции say_hello()
def say_hello(current_hour):
    if current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')
    elif current_hour >= 6 and current_hour <= 11:
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:
        print('Добрый вечер!')

# Дальше код написан без отступов: этот код уже вне функции.

# Несколько раз вызовем функцию say_hello() с разными аргументами:
say_hello(4)  # Вызов функции say_hello() с аргументом 4
say_hello(10)  # Вызов функции с аргументом 10
say_hello(15)  # Ещё один вызов функции
say_hello(20)  # И ещё один вызов




# Здесь объявите функцию say_about()
def say_about():
# Код, написанный ниже, переместите в тело объявленной функции
    print('Привет, я Анфиса!')
    print('Я персональный помощник.')
    print('Я ещё маленькая,')
    print('но постоянно расту и умнею:')
    print('ведь мой код каждый день дописывают!')

# Ниже вызовите объявленную вами функцию say_about()

say_about()


# Объявите функцию здесь
def print_friends_count(friends_count):
    # Код, написанный ниже, переместите внутрь объявленной вами функции
    if friends_count == 0:
        print('У тебя нет друзей')
    elif friends_count == 1:
        print('У тебя', friends_count, 'друг')
    elif friends_count >= 2 and friends_count <= 4:
        print('У тебя', friends_count, 'друга')
    elif friends_count >= 5 and friends_count < 20:
        print('У тебя', friends_count, 'друзей')
    else:
        print('Ого, сколько у тебя друзей! Целых', friends_count)


print_friends_count(15)


def print_friends_count(friends_count):
    if friends_count == 0:
        print('У тебя нет друзей')
    elif friends_count == 1:
        print('У тебя', friends_count, 'друг')
    elif friends_count >= 2 and friends_count <= 4:
        print('У тебя', friends_count, 'друга')
    elif friends_count >= 5 and friends_count < 20:
        print('У тебя', friends_count, 'друзей')
    else:
        print('Ого, сколько у тебя друзей! Целых', friends_count)


# Ниже напишите цикл, в котором будет вызываться функция print_friends_count
# с аргументом от 0 до 20 включительно
for friends_count in range(0, 21):
    print_friends_count(friends_count)

