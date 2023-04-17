from random import random
from tkinter.messagebox import showinfo

def alerta():
    showinfo(
        title='Alerta!',
        message='Dimensões inválidas para ajuste!'
    )

def cores_aleatorias(end = 0xffffff):
    return '#%06X' % round(random() * end)
