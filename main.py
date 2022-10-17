from tkinter import *
from tkinter import ttk
import pyautogui as pg


def carrier_specific_fill():
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

    pg.press('y')
    pg.press('tab')

    pg.click(1813, 191)


def quote_results_fill():
    pg.click(1072, 535)
    pg.click(1278, 715)

    pg.click(1301, 660)

    pg.click(1301, 660)


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Carrier Specific Fill", command=carrier_specific_fill).grid(column=2, row=0)
#ttk.Button(frm, text="Quote Results Fill", command=quote_results_fill).grid(column=3, row=0)
root.mainloop()
