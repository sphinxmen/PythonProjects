from tkinter import *
import random
import tkinter.messagebox as mb

# Рисуем окно

window = Tk()
window.title("Поиграем в Морской бой")
window.geometry('700x280')
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)

# тела всех возможных кораблей
list_ships = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]


# Класс доска
class Boadr:
    def __init__(self):
        # Тут будем хранить кнопки для отрисовки на доске
        self.button = []
        self.lable = None
        self.board_one = []
        self.board_two = []
        self.play_one = 0
        self.p_one_ships = []
        self.p_two_ships = []
        for i in range(200):
            row, col = divmod(i, 20)
            self.button.append(
                Button(window, text=i, width=2, height=1, textvariable=str(i+1),
                       command=self.callback(i)))

            # Разделяем Игровые доски, пока только паддингом, вторую доску рисовать пока не очень хочется, но нужно
            if col == 10:
                padding = 40
            else:
                padding = 1
            if col < 10:
            # if col % 2:
                self.board_one.append(i)
            else:
                self.board_two.append(i)
            self.button[i].grid(row=row + 1, column=col + 1, padx=(padding, 1), pady=1)

        if self.answer_random():
            print(self.board_two)
            self.lock_board()
            p_one = matrix(self.board_one)
            p_one = Randoms(p_one._matrix())
            self.p_one_ships = (p_one._randoms())
            print(self.p_one_ships)
            p_two = matrix(self.board_two)
            p_two = Randoms(p_two._matrix())
            self.p_two_ships = (p_two._randoms())
            print(self.p_two_ships)
        else:
            mb.showerror("Ой ой ой", "Данная функция не доступна в вашей версии, поставьте 12 - баллов")
            mb.showerror("Warning", "Вы согласились с предыдущем предложением поставить 12 баллов")
            exit()
        # Растановка корабрей Random

    def answer_random(self):
        answer = mb.askyesno(
            title="Random",
            message="Раскидать корабли по полям?")
        if answer:
            mb.showinfo("Все уже готово", "Приятной игры")
            return True
        elif not answer:
            mb.showinfo("Удачи", "ну тогда сами расставляйте")
            return False

    def manual(self):
        pass

    # колбек при нажатии на кнопку
    def callback(self, i):
        def _callback():
            # Ships(self.button[i], list_ships)
            if i in self.p_one_ships or i in self.p_two_ships:

                # Собираем строку для отображения
                str = f"Попал, {self.button[i].cget('textvariable')}, {self.button[i]}"
                # Изменяем состояние кнопки, что б не хранить результат ходов
                self.button[i].configure(text='X', state=DISABLED, bg="red", fg="black")
                if (i) in self.board_two:
                    self.p_two_ships.remove(i)
                    # print(self.p_two_ships)
                    self.board_two.remove(i)
                else:
                    self.p_one_ships.remove(i)
                    # print(self.p_one_ships)
                    self.board_one.remove(i)
            else:

                # Изменяем состояние кнопки, что б не хранить результат ходов
                self.button[i].configure(text='*', width=2, height=1, state=DISABLED, fg="red", bg="gray")
                if (i) in self.board_two:
                    self.board_two.remove(i)
                else:
                    self.board_one.remove(i)
                # Дебаг в консоль
                print("Значение: ", self.button[i].cget("textvariable"), self.button[i])
                print(i)
                self.lock_board(0)
                str = f"ПРОМАХ!!!! Значение: , {self.button[i - 1].cget('textvariable')}, {self.button[i]}"
            # Меням Заголовок окна, с отображением хода, в другое место пока не понятно как выводить
            window.title(str)
            if not len(self.p_two_ships):
                mb.showinfo("Game Over", "Победил Player 1")
                self.lock_board(1)
            elif not len(self.p_one_ships):
                mb.showinfo("Game Over", "Победил Player 2")
                self.lock_board(1)

        return _callback

    def lock_board(self, game=0):
        color = "blue"
        if not game:
            if self.play_one:
                for y in self.board_two:
                    self.button[y].configure(state=DISABLED)
                for y in self.board_one:
                    self.button[y].configure(state=ACTIVE)
                self.play_one = 0
            else:
                color = "green"
                for y in self.board_two:
                    self.button[y].configure(state=ACTIVE)
                for y in self.board_one:
                    self.button[y].configure(state=DISABLED)
                self.play_one = 1
            Label(window, text=f"Ход Игрока {self.play_one}", relief=RAISED, fg=color).grid(row=2, column=300, padx=25,
                                                                                            pady=1)
        else:
            for y in self.board_two:
                self.button[y].configure(state=DISABLED)
            for y in self.board_two:
                self.button[y].configure(state=DISABLED)


# Тут мы делаем матрицу, так по ней удобнее расставлять корабли
class matrix:
    def __init__(self, list_buttons):
        self.list_buttons = list_buttons
        self.my_list = list([[] for l in range(0, 10)])

    def _matrix(self):
        count = 0
        y = 0
        for i in self.list_buttons:
            if count == 10:
                y += 1
                count = 0
            self.my_list[y].append(i)
            count += 1
        return self.my_list


# Бегаем по матрице и рандомно выбераем кнопку
# возвращаем все списком, так как по нему быстрее всего отследить попадание
class Randoms:
    def __init__(self, list_player_buttons, players=0):
        self.list_player_buttons = list_player_buttons
        self.ships = []
        self.list_out = []
        self.players = players

    def _randoms(self):
        print(self.list_player_buttons)
        for i in range(len(self.list_player_buttons)):
            list_row = random.randint(0, 9)
            start_pount = 9 - random.randint(0, 9)
            if list_ships[i] + start_pount < 10:
                self.ships.append(list(
                    range(self.list_player_buttons[i][start_pount],
                          self.list_player_buttons[i][start_pount] + list_ships[i])))
            else:
                start_pount -= list_ships[i]
                if 0 > start_pount < list_ships[i]:
                    start_pount = 10 % list_ships[i] + list_ships[i]
                self.ships.append(
                    list(range(self.list_player_buttons[i][start_pount],
                               self.list_player_buttons[i][start_pount] + list_ships[i])))
            self.list_out = [x for l in self.ships for x in l]
        # print(self.list_out)
        return self.list_out

# Ручная расстановка кораблей
class manual:
    def __init__(self, list_player_buttons):
        self.ships = []
        self.list_out = []

    def _manual(self):
        pass


Boadr()

window.mainloop()
