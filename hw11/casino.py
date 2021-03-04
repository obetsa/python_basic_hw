"""
    Casino

    ** для высшего балла хранить статистику игроков в файле
        и при каждом запуске casino запрашивать имя игрока.

    При запуске программы:
        - игроку необходимо ввести имя
        - попадаем в Главное меню
        * возможно у игрока должно быть изначально какое-то количество очков

    Главное меню:
    1. Magic
    2. Blackjack (21)
    3. Посмотреть статистику
    4. Сбросить игровой прогресс

    При выборе пункта 1.
        - выводятся правила игры
        - запускается игра magic (hw3/magic.py)
        - в игре ограниченное количество попыток
        * придумать правила начисления очков при угадывании с 1, 2 .. N попыток
        * придумать правила потери очков при проигрыше

    При выборе пункта 2.
        - выводятся правила игры
        - игрок делает ставку (не больше, чем у него имеется очков)
        - запускается игра blackjack (21)

    При выборе пункта 3.
        - выводится подробная статистика игрока:
            Имя игрока: Max
            Количество очков: 190

            Magic
            Всего игр сыграно: 20
            Выиграно: 5
            Коэффициент выигрышей: 0.25
            Рекордное количество попыток: 2

            Blackjack
            Всего игр сыграно: 0
            Выиграно: 0
            Коэффициент выигрышей: -

    При выборе пункта 4.
        - удаляются данные игрока
        - запрашивается имя нового игрока
        - попадаем в Главное меню


    Реализаци blackjack (правила https://en.wikipedia.org/wiki/Blackjack):
        - формируется колода карт
            от двойки до десятки — от 2 до 10 соответственно,
            у туза — 1 или 11 (11 пока общая сумма не больше 21, далее 1),
            у т.н. картинок (король, дама, валет) — 10.

            в итоге колода - [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

        - колода перетосовывается с помощью random.shuffle()
        - игроку предлагается на выбор:
            1. взять ещё карту
                - из колоды исключается одна карта и дается игроку
            2. остановиться

        - если у игрока в сумме выходит 21 - победа (игроку возвращается удвоенная ставка)
        - если у игрока в сумме выходит больше 21 (перебор) - проигрыш (ставка снимается в пользу казино)
        - если игрок остановился на сумме меньше 21 - ставка возвращается игроку

        * описынные выше правила можно дополнить по желанию
"""