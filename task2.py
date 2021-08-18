'''2. Суммы
Выполнил: Джалилзода Д.Б.
'''


from itertools import product


def cin():
	'''Чтение входных данных с консоли.
	На первой строке вводится натуральное число N — количество чисел в множестве.
	Далее следует N целых чисел, составляющих множество, каждое на отдельной строке.
	'''
	
	#множество чисел
	array = list()

	N = int(input("N = "))
	
	#формирование множества
	for i in range(N):
		n = int(input("n{} = ".format(i + 1)))
		array.append(n)

	return array


def main():
	'''Имеется множество чисел. Найти все разные суммы этих чисел.
	Выводятся всевозможные попарные суммы чисел из множества в порядке
	убывания без повторений. Сумму числа с самим собой тоже считать.
	'''

	#array = [1,4,6,7,2,3,3,3,10]
	array = cin()
	#оставляем только уникальные числа из множества
	array = set(array)

	#составляем всевозможные парфы чисел из множества в порядке повторений
	pairs = list(product(array, array))

	#словарь для хранения всех пар чисел, сумма которых равна
	sums = dict()
	for pair in pairs:
		key = sum(pair)
		if key in sums.keys():
			sums[key].append(pair)
		else:
			sums[key] = [pair,]

	keys = list(sums.keys())
	#сортируем суммы в порядке убывания
	keys.sort()
	keys.reverse()

	#для красивого вывода всех пар чисел в виде a + b = ... = y + z
	sigma = lambda array: ' = '.join([' + '.join(map(str, pair)) for pair in array])

	#выводим пары для уникальных сумм
	for key in keys:
		#print(key, '=', sums[key])
		print(key, '=', sigma(sums[key]))


if __name__ == "__main__":
	main()