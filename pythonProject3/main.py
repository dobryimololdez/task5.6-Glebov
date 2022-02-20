def greet():
    print("________________")
    print("игра крестики- нолики")
    print("формат ввода: x y \n"
          "x - номер строки,  y - номер столбца")
greet()

field = [
    [" "] * 3 for i in range(3)
]

def show_field():
    print()
    print(" | 0 | 1 | 2 | ")
    print(" --------------")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print(" -------------")
    print()
show_field()

def ask_coord():
    while True:
        x, y = map(int, input("   ваш ход:  ").split())

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Координаты вне допустимых значений!")
            continue
        if field[x][y] != " ":
            print(" Клетка занята, повторите ввод!")
            continue
        return x, y
ask_coord()

def check_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
                 ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1 ,2), (2, 2)),
                 ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))
    for cord in win_coord:
        symbols = []
        for i in cord:
            symbols.append(field[i[0]][i[1]])
        if symbols == ["X", "X", "X"]:
            print("X epic wins!")
            return True
        if symbols == ["O", "O", "O"]:
            print("Zero crushed X!")
            return True
    return False


moves = 0
while True:
    moves += 1
    show_field()
    if moves % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")
    x, y = ask_coord()
    if moves % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"
    if check_win():
        break
    if moves == 9:
        print("ничья!")
        break