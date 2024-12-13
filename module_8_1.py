def add_everything_up(a, b):
    try: # код с возможной ошибкой
        return a + b
    except TypeError:  # блок кода в слу. ошибки
        return f"{a}{b}"

# Примеры
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))