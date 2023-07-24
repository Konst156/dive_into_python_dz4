# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def create_argument_dict(**kwargs):
    argument_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        argument_dict[value] = key
    return argument_dict


result = create_argument_dict(a=1, b=[2, 3, 4], c={'x': 5, 'y': 6}, d={1, 2, 3})
print(result)
