from random import choice
from tkinter import *
from Button import *
def mouse_motion(e):
    global mouse_x, mouse_y
    mouse_x, mouse_y = e.x, e.y
    if game_over ==0:
        for i in mode:
            if buttons[i].get_x()<= mouse_x <= buttons[i].get_x()+BUTTON_SIZE and buttons[i].get_y()<= mouse_y <= buttons[i].get_y()+BUTTON_SIZE:
                buttons[i].update_button('chosen')
            else:
                buttons[i].update_button('white')
def mouse_click(e):
    global steps, attemps, game_over
    if game_over == 0:
        for i in mode:
            if buttons[i].get_x() <= mouse_x <= buttons[i].get_x() + BUTTON_SIZE and buttons[i].get_y() <= mouse_y <= buttons[i].get_y() + BUTTON_SIZE:
                check_for_letter(i)
                break
        if attemps <= 0:
            game_over = True
            canvas.itemconfig(word_id, text='Вы проиграли! :(')
def check_for_letter(i):
    global attemps
    if i in word[0]:
        buttons[i].update_button('correct')
        word_update(i)  
    else:
        buttons[i].update_button('wrong')
        attemps -= 1
        canvas.itemconfig(number_id, text=f'Попыток: {attemps}')
                
def key_press(e):
    letter = e.char
    if letter in mode:
        check_for_letter(letter)
    
def word_generation(words):
    word = choice(words)
    hidden_word = '_'*len(word)
    return [word, hidden_word]
def word_update(letter):
    global hidden_word, game_over
    a = list(hidden_word)
    indexes = [i for i in range(len(word[0])) if word[0][i]==letter]
    for j in indexes:
        a[j] = letter
    hidden_word = ''.join(a)
    canvas.itemconfig(word_id, text=hidden_word)
    if hidden_word == word[0]:
        canvas.itemconfig(number_id, text='Победа!')
        game_over = True
words = [x[:-1] for x in open('words.txt')]
rus_letters = sorted('йцукенгшщзхъфывапролджэячсмитьбюё')
eng_letters = sorted('qwertyuiopasdfghjklzxcvbnm')
mode = rus_letters
attemps = 6
steps = 0
mouse_x = mouse_y = 0
game_over = False
window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width = 900
height = 800
x = screen_width // 2 - width // 2
y = screen_height // 2 - height // 2
window.title('Угадайте слово!')
window.geometry(f'{width}x{height}+{x}+{y}')
canvas = Canvas(window, width=width, height=height, background='white')
canvas.create_line(0, height//2, width, height//2)
word = word_generation(words)
hidden_word = word[1]
word_id = canvas.create_text(width//2, height//4, text=word[1], font="Arial 20", anchor=CENTER)
number_id = canvas.create_text(width//8*7, height//8, text=f'Попыток: {attemps}', font="Arial 20", anchor=CENTER)
buttons = {}
i = 0
for y in range(height//2, height, 100):
    for x in range(0, width, 100):
        try:
            symbol = mode[i]
            button = Key(canvas, symbol.upper(), x, y)
            buttons[mode[i]]= button
            i += 1
        except:
            break
canvas.pack(expand=True, fill=BOTH)
window.bind('<Button>', mouse_click)
canvas.bind('<Motion>', mouse_motion)
window.bind('<Key>', key_press)
window.mainloop()