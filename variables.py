"""
3. Выбрать объект для описания из списка: овощ, еда, сотрудник, игрушка (так же можно придумать свой)
4. Объявить переменные основных типов данных для описания этого объекта:

Например объект школьник:
имя (тип строка), возраст (тип целое число), класс (тип целое число), отличник или нет (логический тип), средняя оценка (число с плавающей точкой)

Чем больше переменных (характеристик), тем лучше. Минимально 4 переменные для типов (строка, число, число с плавающей точкой, логический тип)

5. В конце модуля с помощью функции type вывести тип для каждой из объявленных переменных
"""

# Объект овощ
name = "Огурец"
# Срок созревания
ripening_period = 40
# Средний вес в кг
the_weight = 0.05
# Многолетнее
perennial = False

print(type(name))
print(type(ripening_period))
print(type(the_weight))
print(type(perennial))
