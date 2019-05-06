#!/usr/bin/env python3.6

import tkinter
from tkinter import ttk
import softphone, config


root = tkinter.Tk()
root.title('{} - {}'.format(config.APP_NAME, config.APP_VERSION))
root.resizable(False, False)
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file=config.APP_ICON))

def on_closing():
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_closing)

softphone.Softphone(root).run()

if __name__ == '__main__':
    root.mainloop()