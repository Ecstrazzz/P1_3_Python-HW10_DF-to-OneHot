"""
Знакомство с языком Python (семинары)

Урок 10. Построение графиков

Задача 44: В ячейке ниже представлен код генерирующий
DataFrame, которая состоит всего из 1 столбца. Ваша
задача перевести его в one hot вид. Сможете ли вы это
сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

Статья про one hot вид: https://colab.research.google.com/drive/1qKamnDiRmpRZkpiqWPkunBdAhmzhMcGz?usp=sharing

Формат сдачи: ссылка на свой репозиторий
"""

import random
import pandas as pd
from tabulate import tabulate

# Создание списка и DataFrame
lst = ["robot"] * 10 + ["human"] * 10
random.shuffle(lst)
data = pd.DataFrame({"whoAmI": lst})

# Первоначальный вывод DataFrame (первые 5 элементов)
# print(data.head())
print(tabulate(data.head(), headers='keys', tablefmt='grid'))

# Преобразование DataFrame
data = data.groupby(data.index).apply(lambda x: pd.Series(1, index=x["whoAmI"]))
data = data.unstack(fill_value=0)

# Вывод преобразованного DataFrame (первые 5 элементов)
# print(data.head())
print(tabulate(data.head(), headers='keys', tablefmt='grid'))
