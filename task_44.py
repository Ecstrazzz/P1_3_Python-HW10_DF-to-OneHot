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

