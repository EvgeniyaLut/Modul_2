playlist = {
    'Venus',
    'Yesterday',
    'Fireball',
    'Time',
    'Poison'
}

playlist.add('Thunderstruck')
print(playlist)
# Будет напечатано:
# {'Yesterday', 'Fireball', 'Thunderstruck', 'Poison', 'Venus', 'Time'}
# Элементы множеств никогда не соблюдают порядок!




playlist_1 = {'Три белых коня', 'Happy new year', 'Снежинка'}
playlist_2 = {'Last christmas', 'Снежинка', 'Happy new year'}
playlist_3 = playlist_1.union(playlist_2)

print(playlist_3)


playlist_1 = {'Голубой вагон', 'Облака', 'Yesterday', 'Наше лето'}
playlist_2 = {'Наше лето', 'Голубой вагон', 'Облака'}
playlist_3 = playlist_1.difference(playlist_2)

print(playlist_3)


def print_valid_cities(all_cities, used_cities):
    a = all_cities.difference(used_cities)
    for city in a:
        print(city)

    # Вместо этого многоточия напишите код функции, она должна
    # принимать и обрабатывать аргументы all_cities и used_cities,
    # а затем печатать результат в нужном формате


all_cities = {
    'Абакан',
    'Астрахань',
    'Бобруйск',
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк',
    'Новосибирск'
}

used_cities = {'Калуга', 'Абакан', 'Новосибирск'}

print_valid_cities(all_cities, used_cities)




def print_valid_cities(all_cities, used_cities):
    diff = all_cities.difference(used_cities)
    for city in diff:
        print(city)


def add_cities(all_cities, new_cities):
    all_cities.add(new_cities)


# Анфиса нашла названия нескольких новых городов,
# эти города нужно добавить в множество all_cities
new_cities = [
    'Екатеринбург',
    'Выборг' ,
    'Владивосток',
    'Казань',
    'Why',
    'Йезд'
]

all_cities = {
    'Абакан',
    'Астрахань',
    'Бобруйск',
    'Калуга',
    'Караганда',
    'Кострома',
    'Липецк',
    'Новосибирск'
}

used_cities = {
    'Калуга',
    'Абакан' ,
    'Новосибирск'
}

add_cities(all_cities, new_cities)
print_valid_cities(all_cities, used_cities)