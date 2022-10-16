# Чему равно значение выражения?

src = not False and True or False and not True
# result = True and True or False and False # производим инверсию
# result = True or False # производим конъюнкцию
# result = True # производим дизъюнкцию

result = True

print(src == result)
