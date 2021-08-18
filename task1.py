'''1. Пинг - понг
Выполнил: Джалилзода Д.Б.
'''


from re import match as regex_check


class ScoreError(Exception):
    """Исключение вызывается при неправильном формате входных данных
    """

    def __init__(self, message="Неправильный формат входных данных!"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return 'Функция принимает единственный аргумент score, который представляет собой счет игры в виде строки "Z:Z", где Z - целое число больше 0.'


def service(score):
    '''Функция принимает текущий счет в виде строки,
    разделенной знаком ":" как единственный параметр и возвращает "first"
    или "second" в зависимости от того, чья сейчас очередь подавать.

    Игроки сменяются после каждых 5 подач пока счет не
    станет 20:20 - с этого момента каждый игрок подает 2 раза.
    '''

    delimeter = ":"
    turns = {0: 'first', 1: 'second'}

    #проверка правильности входных данных
    regex = "^[0-9]*" + delimeter + "[0-9]*$"
    if regex_check(regex, score):
        first, second = map(int, score.split(delimeter))
    else:
        raise ScoreError("Неправильный ввод!")

    total = first + second #столько подач разыграно

    #применяем правило количества подач подряд
    if first >= 20 and second >= 20:
        pitches = 2
    else:
        pitches = 5

    #начинает первый игрок
    turn = turns[0]
    for pitch in range(1, total):
        #определяем, чья очередь подавать
        if pitch % pitches == pitches - 1:
            turn = turns[1] if turn == turns[0] else turns[0]

    return turn


def test():
    scores = ["0:0", "3:2", "21:20", "21:22"]

    for score in scores:
        print(service(score))


def test_full(n=30):
    for i in range(n):
        for j in range(n):
            score = f"{i}:{j}"
            print(score, service(score))


if __name__ == "__main__":
    test()
    #test_full()