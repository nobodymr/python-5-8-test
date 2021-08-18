'''4. Раскрытие
Выполнил: Джалилзода Д.Б.
'''


def unpack(mix):
    '''Распаковывает список элементов, которые могут содержать
    объекты (int, str, list, tuple, dict, set) друг в друге без
    предопределенной глубины. что означает, что может быть много
    уровней элементов, содержащихся друг в друге.
    '''

    unpacked = list()
    while mix: #Пока в списке есть элементы
        elem = mix.pop()
        if type(elem) in (list, tuple, set): #Проверяем тип элемента
            mix.extend(elem) #Добавляем элемент в список
        elif isinstance(elem, dict):
            mix.extend(elem.keys())
            mix.extend(elem.values())
        else:
            unpacked.append(elem) #Не итерируемый тип или строка
    return unpacked[::-1] # восстанавливаем порядок элементов


mix = [None, [1, ({2, 3, 5}, {'foo': 'bar'})]] #[None, 1, 2, 3, 'foo', 'bar']
print(unpack(mix))