from tkinter import *
from tkinter import ttk
import pyautogui as pg


screenWidth, screenHeight = pg.size()

#this is a test.


def move_click():
    pg.doubleClick(1693, 348)
    pg.press('y')
    pg.press('tab')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')

    pg.typewrite('ot')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')

    pg.press('y')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')

    pg.press('n')
    pg.press('tab')

    pg.press('y')
    pg.press('tab')

    pg.press('y')
    pg.press('tab')




root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="click", command=move_click).grid(column=2, row=0)
root.mainloop()