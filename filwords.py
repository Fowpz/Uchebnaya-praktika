import tkinter as tk
from tkinter import messagebox, Label, Button
import random

class FillwordGame:
    def __init__(self, master):
        self.master = master
        self.cell_size = 50
        self.selected_cells = []
        self.guessed_words = set()
        self.score = 0
        self.level = 1

        self.word_colors = {}      
        self.cell_to_word = {}     

        self.available_colors = [
            "#a8d8a8", "#ffd1dc", "#add8e6", "#ffffb3", "#ffcccb", "#c5cae9",
            "#d1c4e9", "#b2dfdb", "#ffe0b2", "#f0f4c3", "#f8bbd0", "#c8e6c9"
        ]

        self.levels = [
            {
                'size': 5,
                'words': {
                    "РАКЕТА": [0, 1, 2, 3, 4, 9],
                    "КОМЕТА": [5, 10, 15, 20, 21, 22],
                    "КОРАБЛЬ": [10, 11, 12, 13, 18, 19, 24],
                    "ВЕНЕРА": [11, 6, 7, 8, 13, 18]
                },
                'grid': [
                    "Р", "А", "К", "Е", "Т",
                    "К", "Е", "Н", "Е", "А",
                    "О", "В", "К", "Р", "А",
                    "М", "А", "О", "Б", "Л",
                    "Е", "Т", "Р", "А", "Ь"
                ]
            },
            {
                'size': 7,
                'words': {
                    "ФУТБОЛ": [0, 8, 16, 24, 32, 40],
                    "БАСКЕТБОЛ": [1, 10, 19, 28, 29, 30, 31, 38, 39, 40],
                    "ГОЛЬФ": [42, 43, 44, 45, 46],
                    "ГИМНАСТИКА": [4, 11, 18, 25, 26, 27, 28, 35, 36, 37],
                    "ТЕННИС": [3, 10, 17, 24, 31, 38],
                    "ХОККЕЙ": [6, 13, 20, 27, 34, 41],
                    "БОУЛИНГ": [5, 12, 19, 26, 33, 40, 41]
                },
                'grid': [
                    "Ф", "Б", "Г", "Т", "Е", "Н", "Н",
                    "У", "А", "И", "Х", "О", "К", "И",
                    "Т", "С", "М", "Н", "Е", "К", "С",
                    "Б", "К", "Л", "А", "Й", "У", "Л",
                    "О", "Е", "О", "С", "Б", "О", "И",
                    "Л", "Т", "Б", "Т", "И", "К", "Н",
                    "Г", "О", "Л", "Ь", "Ф", "А", "Г"
                ]
            },
            {
                'size': 9,
                'words': {
                    "АЛГОРИТМ": [0, 1, 2, 3, 4, 13, 22, 31],
                    "СХЕМА": [9, 18, 27, 36, 45],
                    "ПРОГРАММИРОВАНИЕ": [54, 55, 56, 57, 58, 59, 60, 61, 62, 71, 80, 79, 78, 77, 76],
                    "СЕРВЕР": [63, 64, 65, 66, 67, 68],
                    "СТРОКИ": [36, 37, 38, 39, 40, 41],
                    "РАЗРАБОТЧИК": [10, 11, 12, 13, 14, 15, 16, 17, 26, 35],
                    "ПРОЕКТ": [30, 31, 32, 33, 34, 35],
                    "МАКРОС": [45, 50, 41, 32, 23, 14],
                    "АЙПИ": [19, 28, 37, 46],
                    "ОТКЛАДКА": [4, 5, 6, 7, 8, 17, 26, 35],
                    "КАПЧА": [22, 23, 24, 33, 42]
                },

                'grid': [
                    "А", "Л", "Г", "О", "Т", "К", "Л", "А", "Д",
                    "С", "Р", "О", "З", "Р", "А", "Б", "О", "К",
                    "Х", "И", "Р", "А", "К", "А", "П", "Т", "А",
                    "Е", "Т", "М", "П", "Р", "А", "Ч", "Ч", "И",
                    "М", "С", "С", "И", "О", "Е", "К", "Т", "К",
                    "А", "Е", "Т", "К", "Р", "О", "В", "А", "Н",
                    "П", "Р", "Р", "О", "И", "М", "С", "А", "И",
                    "Р", "В", "Е", "Р", "М", "А", "О", "Й", "Е",
                    "О", "Г", "Р", "А", "М", "К", "Р", "П", "И"
                ]
            }
        ]

        self.setup_main_menu()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()


    def setup_main_menu(self):
        self.clear_window()
        self.master.title("ФИЛВОРДЫ")
        self.master.geometry("1200x800")
        self.master.configure(bg='#e8caca')
        self.master.resizable(False, False)

        Label(self.master, text='ФИЛВОРДЫ', font=("Bahnschrift SemiBold Condensed", 68), bg="#e8caca", fg="#1E1E1E").place(x=425,
                                                                                                                        y=100)

        Button(self.master, text="ИГРАТЬ", font=("Bahnschrift SemiBold Condensed", 27), width=23, height=3,
               background='#ebdfdf', foreground='#000000', command=self.start_game).place(x=425, y=600)

        Button(self.master, text="ПРАВИЛА ИГРЫ", font=("Bahnschrift SemiBold Condensed", 20), width=23, height=3,
               background='#ebdfdf', foreground='#000000', command=self.show_rules).place(x=105, y=620)

        Button(self.master, text="ВЫЙТИ ИЗ ИГРЫ", font=("Bahnschrift SemiBold Condensed", 20), width=23, height=3,
               background='#ebdfdf', foreground='#000000', command=self.master.quit).place(x=810, y=620)

    def show_rules(self):
        self.clear_window()
        for widget in self.master.winfo_children():
            widget.place_forget()

        rules = [
            "                               Цель – найти в сетке букв необходимое количество слов для перехода на следующий уровень.",
            "                               Игрок соединяет буквы левой кнопкой мыши только под прямым углом.",
            "                               Слова могут быть расположены: слева направо, справа налево, сверху вниз, снизу вверх.",
            "                               За правильно найденное слово начисляется 15 очков.",
            "                               Очки можно тратить на подсказки. Подсказок можно использовать сколько угодно.",
            "                               Победа достигается, если найдены все слова на уровне.",
            "                               Поле — сетка из букв размером NxN."
        ]

        Label(self.master, text='Правила игры', font=('Bahnschrift SemiBold Condensed', 30), bg="#e8caca",
              fg="#1E1E1E").place(x=415, y=50)

        for i, rule in enumerate(rules):
            Label(self.master, text=rule, font=('Bahnschrift SemiBold Condensed', 16), wraplength=1000,
                  bg="#e8caca", fg="#1E1E1E", justify="left").place(x=100, y=150 + i * 40)

        Button(self.master, text='НАЗАД В МЕНЮ', font=("Bahnschrift SemiBold Condensed", 24), width=25, height=2,
               background='#ebdfdf', foreground='#000000', command=self.setup_main_menu).place(x=390, y=620)

    def start_game(self):
        self.master.withdraw()
        self.selected_cells = []
        self.guessed_words = set()
        self.score = 0
        self.level = 1
        self.word_colors = {}
        self.cell_to_word = {}
        self.open_level()

    def open_level(self):
        self.game_window = tk.Toplevel(self.master)
        self.selected_cells = []
        self.guessed_words = set()
        self.word_colors = {}
        self.cell_to_word = {}

        self.game_window.title("Филворды")
        self.game_window.geometry("1200x800")
        self.game_window.configure(bg='#e8caca')
        self.game_window.resizable(False, False)
        self.game_window.protocol("WM_DELETE_WINDOW", self.back_to_menu)

        self.size = self.levels[self.level - 1]['size']
        self.cell_size = 600 // self.size
        self.visible_grid = [["" for _ in range(self.size)] for _ in range(self.size)]

        self.canvas = tk.Canvas(self.game_window, width=self.cell_size * self.size,
                                height=self.cell_size * self.size, bg='#ebdfdf')
        self.canvas.place(x=300, y=100)

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.score_label = Label(self.game_window, text=f"Баланс: {self.score}",
                                font=("Bahnschrift SemiBold Condensed", 16), bg='#e8caca')
        self.score_label.place(x=930, y=80)

        Button(self.game_window, text="ПОДСКАЗКА (-30)", font=("Bahnschrift SemiBold Condensed", 16), width=23, height=2,
            background='#ebdfdf', foreground='#000000', command=self.use_hint).place(x=940, y=600)

        Button(self.game_window, text="ВЫЙТИ В ГЛАВНОЕ МЕНЮ", font=("Bahnschrift SemiBold Condensed", 15), width=25, height=2,
            background='#ebdfdf', foreground='#000000', command=self.back_to_menu).place(x=930, y=700)

        Button(self.game_window, text="СБРОСИТЬ", font=("Bahnschrift SemiBold Condensed", 15), width=23, height=2,
            background='#f5b5b5', foreground='#000000', command=self.reset_level).place(x=940, y=500)

        
        self.initial_score_for_level = self.score

        self.load_grid()
        self.draw_grid()


    def back_to_menu(self):
        if hasattr(self, 'game_window'):
            self.game_window.destroy()
        self.master.deiconify()
        self.setup_main_menu()

    def load_grid(self):
        level_data = self.levels[self.level - 1]
        grid_letters = level_data['grid']

        for i in range(self.size):
            for j in range(self.size):
                self.visible_grid[i][j] = grid_letters[i * self.size + j]

        self.remaining_words = list(level_data['words'].keys())  

    def draw_grid(self):
        self.canvas.delete("all")
        for i in range(self.size):
            for j in range(self.size):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                fill_color = '#ebdfdf'  
                if (i, j) in self.guessed_words:
                    word = self.cell_to_word.get((i, j))
                    if word:
                        fill_color = self.word_colors.get(word, '#a8d8a8')

                elif (i, j) in self.selected_cells:
                    fill_color = '#f0a2a2'

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline='black')
                self.canvas.create_text(x1 + self.cell_size // 2, y1 + self.cell_size // 2,
                                        text=self.visible_grid[i][j], font=("Bahnschrift SemiBold Condensed", 28))

    def on_click(self, event):
        row, col = event.y // self.cell_size, event.x // self.cell_size
        if 0 <= row < self.size and 0 <= col < self.size:
            if (row, col) not in self.selected_cells:
                if not self.selected_cells:
                    self.selected_cells.append((row, col))
                else:
                    last_row, last_col = self.selected_cells[-1]
                    if (abs(row - last_row) == 1 and col == last_col) or (abs(col - last_col) == 1 and row == last_row):
                        self.selected_cells.append((row, col))
            self.draw_grid()

    def on_drag(self, event):
        self.on_click(event)

    def on_release(self, event):
        
        word = ''.join([
            self.visible_grid[r][c]
            for r, c in self.selected_cells
            if 0 <= r < self.size and 0 <= c < self.size
        ]).upper()

        if word in self.remaining_words:
            
            self.guessed_words.update(self.selected_cells)
            self.remaining_words.remove(word)
            self.score += 15
            self.score_label.config(text=f"Баланс: {self.score}")

            word_color = self.available_colors[len(self.word_colors) % len(self.available_colors)]
            self.word_colors[word] = word_color
            for cell in self.selected_cells:
                self.cell_to_word[cell] = word

            if not self.remaining_words:
                if self.level < len(self.levels):
                    self.level += 1
                    messagebox.showinfo("Уровень пройден!", f"Переход на уровень {self.level}")
                    self.game_window.destroy()
                    self.open_level()
                else:
                    self.show_victory_screen_in_game_window()


        self.selected_cells.clear()
        self.draw_grid()

    def reset_level(self):
        self.score = self.initial_score_for_level  
        self.score_label.config(text=f"Баланс: {self.score}")
        
        self.selected_cells.clear()
        self.guessed_words.clear()
        self.word_colors.clear()
        self.cell_to_word.clear()
        
        self.load_grid()
        self.draw_grid()


    def use_hint(self):
        if self.score < 30:
            messagebox.showinfo("Недостаточно очков", "Для подсказки нужно минимум 30 очков.")
            return

        if not self.remaining_words:
            messagebox.showinfo("Подсказка", "Все слова уже найдены.")
            return

        hint_word = random.choice(self.remaining_words)
        first_letter = hint_word[0]

        self.score -= 30
        self.score_label.config(text=f"Баланс: {self.score}")

        messagebox.showinfo("Подсказка", f"Первая буква одного из слов: {first_letter}")

    def show_victory_screen_in_game_window(self):
        
        for widget in self.game_window.winfo_children():
            widget.destroy()

        self.game_window.title("ПОБЕДА!")
        self.game_window.geometry("1200x800")
        self.game_window.configure(bg='#e8caca')

        Label(self.game_window, text="УРА, ВЫ ПОБЕДИЛИ =)", font=("Bahnschrift SemiBold Condensed", 36),
            bg='#e8caca', fg="#1E1E1E").place(x=410, y=300)

        Button(self.game_window, text="В ГЛАВНОЕ МЕНЮ", font=("Bahnschrift SemiBold Condensed", 24), width=25, height=2,
            background='#ebdfdf', foreground='#000000', command=self.back_to_menu).place(x=390, y=500)





if __name__ == "__main__":
    root = tk.Tk()
    app = FillwordGame(root)
    root.mainloop()
