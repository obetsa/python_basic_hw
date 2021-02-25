"""
    1. Реализовать функцию get_country(city), которая принимает название города
    и возвращает страну, которой он принадлежит исходя из словаря data.

    2. Релизовать функцию groupping_data(data), которая принимает словарь data
    и возвращает отформатированные данные в виде списка словарей с ключами
    'country', 'capital' и 'cities'.
    Учитывать, что во входящем словаре data
    ключ - country, первый элемент значения - capital, остальные - cities.
"""

data = {
    "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
    "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
    "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
    "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
}


def get_country(city):
    for k, v in data.items():
        if city in v:
            print(k)
    return city


data = {
    "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
    "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
    "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
    "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
}
city = input('city: ')
get_country(city)


def groupping_data(data):
    geodata = []
    for k, v in data.items():
        country = {}
        country['country'] = k
        country['capital'] = v[0]
        country['cities'] = v[1] + ', ' + v[2] + ', ' + v[3]
        geodata.append(country)
    return geodata


for i in range(len(groupping_data(data))):
    print(groupping_data(data)[i].items())
