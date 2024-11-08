# На вход программе подается строка с названиями городов,
# записанных в одну строчку через пробел.
# Необходимо ее прочитать и применить функцию map так,
# чтобы она возвращала названия городов только длиной
# более 5 символов. Вместо остальных названий - строку
# с дефисом ("-").
def names_cities(func: callable, str1: str):

    str1 = str1.split()
    new_str = []
    for city in str1:
        c = func(city)
        new_str.append(c)
    new_str1 = " ".join(new_str)
    return new_str1


def filter_city(city):
    if len(city) > 5:
        return city
    else:
        return "-"


_str = "Москва Уфа Вологда Тула Владивосток Хабаровск"

print(names_cities(filter_city, _str))
# Пример:
# Москва Уфа Вологда Тула Владивосток Хабаровск
# Результат:
# Москва - Вологда - Владивосток Хабаровск

# P.S. Очевидно, функцию для передачи в map нужно сделать самому.
