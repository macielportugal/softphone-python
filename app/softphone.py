import os

import tkinter

from tkinter import ttk

import config


class Logo():

    def __init__(self, parent, column, row):
        self.parent = parent
        self.column = column
        self.row = row

    def layout(self):
        self.logo_frame = ttk.Frame(self.parent, height=30, style='LOGO.TFrame')
        self.logo_frame.grid(column=self.column, row=self.row, sticky='we')
        self.logo_frame.grid_propagate(0)
        self.logo_frame.columnconfigure(0, weight=1)
        self.logo_frame.rowconfigure(0, weight=1)    

        image = tkinter.PhotoImage(file=config.APP_LOGO)
        self.logo_image = ttk.Label(self.logo_frame, image=image,
            style='LOGO.TLabel')
        self.logo_image.image = image
        self.logo_image.grid(column=0, row=0)

    def style(self):
        ttk.Style().configure('LOGO.TFrame', 
            background=config.APP_DEFAULT_BACKGROUND_COLOR)
        ttk.Style().configure('LOGO.TLabel', 
            background=config.APP_DEFAULT_BACKGROUND_COLOR, compound='center')

    def run(self):
        self.layout()
        self.style()


class Screen():

    def __init__(self, parent, column, row):
        self.parent = parent
        self.column = column
        self.row = row

    def layout(self):
        self.screen_frame = ttk.Frame(self.parent, height=60, padding=(0, 5, 0, 10),
            style='SCREEN.TFrame')
        self.screen_frame.grid(column=self.column, row=self.row, sticky='we')
        self.screen_frame.grid_propagate(0)
        self.screen_frame.columnconfigure(0, weight=1)
        self.screen_frame.rowconfigure(0, weight=1)

        self.form = ttk.Entry(self.screen_frame)
        self.form.grid(column=0, row=0, sticky='nwes') 

    def style(self):
        ttk.Style().configure('SCREEN.TFrame', background=config.APP_DEFAULT_BACKGROUND_COLOR)

    def run(self):
        self.layout()
        self.style()


class Keyboard():

    def __init__(self, parent, column, row, screen):
        self.parent = parent
        self.column = column
        self.row = row
        self.screen = screen

    def layout(self):
        self.keyboard_frame = ttk.Frame(self.parent, height=370, 
            style="KEYBOARD.TFrame")
        self.keyboard_frame.grid_propagate(0)
        self.keyboard_frame.grid(column=self.column, row=self.row, sticky="we")
        self.keyboard_frame.grid_propagate(0)

        for number in range(0, 3):
            self.keyboard_frame.columnconfigure(number, weight=1)

        for number in range(0, 12):
            self.keyboard_frame.rowconfigure(number, weight=1)

        self.button_answer_frame = ttk.Frame(self.keyboard_frame, padding=2,
            style='KEYBOARDBUTTONSUCCESS.TFrame')
        self.button_answer_frame.grid(column=0, row=0, sticky='nwes')
        self.button_answer_frame.columnconfigure(0, weight=1)
        self.button_answer_frame.rowconfigure(0, weight=1)

        self.button_answer = ttk.Button(self.button_answer_frame, 
            text='Atender', style="KEYBOARDSUCCESS.TButton")
        self.button_answer.grid(column=0, row=0, sticky='nwes')

        self.button_hangup_frame = ttk.Frame(self.keyboard_frame, padding=2,
            style='KEYBOARDBUTTONWARNING.TFrame')
        self.button_hangup_frame.grid(column=2, row=0, sticky='nwes')
        self.button_hangup_frame.columnconfigure(0, weight=1)
        self.button_hangup_frame.rowconfigure(0, weight=1)

        self.button_hangup = ttk.Button(self.button_hangup_frame, 
            text='Desligar', style="KEYBOARDWARNING.TButton")
        self.button_hangup.grid(column=0, row=0, sticky='nwes')

        column = row = 1
        for number in range (0, 9):

            if number % 3 == 0:
                column = 0
                row += 1

            number_frame = 'frame_' + str(number + 1)
            setattr(self, number_frame, ttk.Frame(self.keyboard_frame, 
                padding=2, style='KEYBOARDBUTTONNUMBER.TFrame'))
            getattr(self, number_frame).grid(column=column, row=row, 
                sticky='nwes')
            getattr(self, number_frame).columnconfigure(0, weight=1)
            getattr(self, number_frame).rowconfigure(0, weight=1)
            
            number_text = 'button_' + str(number + 1)
            setattr(self, number_text, ttk.Button(getattr(self, number_frame), 
                text=(number + 1), style='KEYBOARD.TButton'))
            getattr(self, number_text).grid(column=0, row=0, sticky='nwes')

            column += 1

        self.button_ast_frame = ttk.Frame(self.keyboard_frame, padding=2,
            style='KEYBOARDBUTTONNUMBER.TFrame')
        self.button_ast_frame.grid(column=0, row=5, sticky='nwes')
        self.button_ast_frame.columnconfigure(0, weight=1)
        self.button_ast_frame.rowconfigure(0, weight=1)

        self.button_ast = ttk.Button(self.button_ast_frame, text='*', 
            style='KEYBOARD.TButton')
        self.button_ast.grid(column=0, row=0, sticky='nwes')

        self.button_0_frame = ttk.Frame(self.keyboard_frame, padding=2,
            style='KEYBOARDBUTTONNUMBER.TFrame')
        self.button_0_frame.grid(column=1, row=5, sticky='nwes')
        self.button_0_frame.columnconfigure(0, weight=1)
        self.button_0_frame.rowconfigure(0, weight=1)

        self.button_0 = ttk.Button(self.button_0_frame, text='0', 
            style='KEYBOARD.TButton')
        self.button_0.grid(column=0, row=0, sticky='nwes')

        self.button_hash_frame = ttk.Frame(self.keyboard_frame, padding=2,
            style='KEYBOARDBUTTONNUMBER.TFrame')
        self.button_hash_frame.grid(column=2, row=5, sticky='nwes')
        self.button_hash_frame.columnconfigure(0, weight=1)
        self.button_hash_frame.rowconfigure(0, weight=1)

        self.button_hash = ttk.Button(self.button_hash_frame, text='#', 
            style='KEYBOARD.TButton')
        self.button_hash.grid(column=0, row=0, sticky='nwes')

        self.button_pause_frame = ttk.Frame(self.keyboard_frame, padding=2,
            style='KEYBOARDBUTTONALERT.TFrame')
        self.button_pause_frame.grid(column=1, row=7, sticky='nwes')
        self.button_pause_frame.columnconfigure(0, weight=1)
        self.button_pause_frame.rowconfigure(0, weight=1)

        self.button_pause = ttk.Button(self.button_pause_frame, text='Pausar', 
            style='KEYBOARDALERT.TButton')
        self.button_pause.grid(column=0, row=0, sticky='nwes')

        self.button_volume_frame = ttk.Frame(self.keyboard_frame, padding=2,
            style='KEYBOARDBUTTONNUMBER.TFrame')
        self.button_volume_frame.grid(column=0, row=9, columnspan=3)
        self.button_volume_frame.columnconfigure(0, weight=1)
        self.button_volume_frame.columnconfigure(1, weight=1)
        self.button_volume_frame.rowconfigure(0, weight=1)

        image = tkinter.PhotoImage(file=config.APP_ICON_VOLUME_ON)
        self.button_icon_volume = ttk.Button(self.button_volume_frame, image=image, 
            style='KEYBOARDALERT.TButton', compound='image')
        self.button_icon_volume.image = image
        self.button_icon_volume.grid(column=0, row=0)

        self.button_volume = ttk.Scale(self.button_volume_frame,
            orient=tkinter.HORIZONTAL, length=200, from_=1, to=10, value=8)
        self.button_volume.grid(column=1, row=0)

        self.button_microphone_frame = ttk.Frame(self.keyboard_frame, padding=2,
            style='KEYBOARDBUTTONNUMBER.TFrame')
        self.button_microphone_frame.grid(column=0, row=10, columnspan=3)
        self.button_microphone_frame.columnconfigure(0, weight=1)
        self.button_microphone_frame.columnconfigure(1, weight=1)
        self.button_microphone_frame.rowconfigure(0, weight=1)

        image = tkinter.PhotoImage(file=config.APP_ICON_MICROPHONE_ON)
        self.button_icon_volume = ttk.Button(self.button_microphone_frame, image=image, 
            style='KEYBOARDALERT.TButton', compound='image')
        self.button_icon_volume.image = image
        self.button_icon_volume.grid(column=0, row=0)

        self.button_microphone = ttk.Scale(self.button_microphone_frame, 
            orient=tkinter.HORIZONTAL, length=200, from_=1, to=10, value=8)
        self.button_microphone.grid(column=1, row=0)

    def style(self):
        style = ttk.Style()
        style.configure('KEYBOARD.TFrame', foreground='white',
            background=config.APP_DEFAULT_BACKGROUND_COLOR)
        style.configure('KEYBOARDBUTTONNUMBER.TFrame', background='white')
        style.configure("KEYBOARD.TButton", foreground='white', 
            background=config.APP_DEFAULT_BACKGROUND_COLOR, borderwidth=0)
        style.configure('KEYBOARDBUTTONSUCCESS.TFrame', background='green')
        style.configure('KEYBOARDBUTTONWARNING.TFrame', background='red')
        style.configure('KEYBOARDBUTTONALERT.TFrame', background='orange')   
        style.configure('KEYBOARDSUCCESS.TButton', foreground='green', 
            background=config.APP_DEFAULT_BACKGROUND_COLOR, borderwidth=0)
        style.configure('KEYBOARDWARNING.TButton', foreground='red', 
            background=config.APP_DEFAULT_BACKGROUND_COLOR, borderwidth=0)
        style.configure('KEYBOARDALERT.TButton', foreground='orange', 
            background=config.APP_DEFAULT_BACKGROUND_COLOR, borderwidth=0)

    def action_button(self, button):
        if button == 'ast':
            button = '*'

        if button == 'hash':
            button = '#'

        self.screen.form.insert('end', button)
    
    def event(self):
        def act_number(number):
            return lambda e: self.action_button(number)

        buttons = list(range(0, 10)) + ['ast', 'hash']
        for button in buttons:
            button_text = 'button_' + str(button)
            getattr(self, button_text).bind('<Button-1>', act_number(button))

    def run(self):
        self.layout()
        self.style()
        self.event()


class Footer():

    def __init__(self, parent, column, row):
        self.parent = parent
        self.column = column
        self.row = row

    def layout(self):
        self.footer_frame = ttk.Frame(self.parent, height=30,
            style='FOOTER.TFrame')
        self.footer_frame.grid(column=self.column, row=self.row, sticky='we')
        self.footer_frame.grid_propagate(0)
        self.footer_frame.columnconfigure(0, weight=1)
        self.footer_frame.rowconfigure(0, weight=1)    

        self.footer_text = ttk.Label(self.footer_frame, 
            text='Desenvolvido por Skylinks', style='FOOTER.TLabel')
        self.footer_text.grid(column=0, row=0)

    def style(self):
        ttk.Style().configure('FOOTER.TFrame', 
            background=config.APP_DEFAULT_BACKGROUND_COLOR)
        ttk.Style().configure('FOOTER.TLabel', foreground='white',
            background=config.APP_DEFAULT_BACKGROUND_COLOR, compound='center')

    def run(self):
        self.style()
        self.layout()


class Softphone():

    def __init__(self, parent):
        self.parent = parent

    def layout(self):
        self.softphone_frame = ttk.Frame(self.parent, width=300, height=500,
            style="SOFTPHONE.TFrame", padding=15)
        self.softphone_frame.grid(column=0, row=1)
        self.softphone_frame.grid_propagate(0)
        self.softphone_frame.columnconfigure(0, weight=1)
        self.softphone_frame.rowconfigure(0, weight=1)
        self.softphone_frame.rowconfigure(1, weight=1)
        self.softphone_frame.rowconfigure(2, weight=1)

        self.logo = Logo(self.softphone_frame, 0, 0)
        self.screen = Screen(self.softphone_frame, 0, 1)
        self.keyboard = Keyboard(self.softphone_frame, 0, 2, self.screen)
        self.footer = Footer(self.softphone_frame, 0, 3)

    def style(self):
        ttk.Style().configure('SOFTPHONE.TFrame', 
            background=config.APP_DEFAULT_BACKGROUND_COLOR)

    def run(self):
        self.layout()
        self.style()
        self.logo.run()      
        self.screen.run()
        self.keyboard.run()
        self.footer.run()
