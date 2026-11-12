from tkinter.constants import CENTER

BUTTON_SIZE = 100
class Key:
    def __init__(self, canvas, letter, x, y):
        self.__canvas = canvas
        self.__letter = letter
        self.__x = x
        self.__y = y
        self.__create_button(self.__letter)
        self.__color = None
        self.__used = False
    def __create_button(self, letter):
        self.__id = self.__canvas.create_rectangle(self.__x, self.__y, self.__x+BUTTON_SIZE, self.__y+BUTTON_SIZE)
        self.__text_id = self.__canvas.create_text(self.__x+BUTTON_SIZE//2, self.__y+BUTTON_SIZE//2,text=letter, font="Arial 20", anchor=CENTER)
    def update_button(self, state):
        if self.__used == False:
            if state == 'correct':
                self.__color = 'green'
                self.__used = True
            elif state == 'wrong':
                self.__color = 'red'
                self.__used = True
            elif state == 'chosen':
                self.__color = 'blue'
            else:
                self.__color = 'white'
            self.__canvas.itemconfig(self.__id, fill=self.__color)

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_letter(self):
        return self.__letter
    def __str__(self):
        return self.__letter
