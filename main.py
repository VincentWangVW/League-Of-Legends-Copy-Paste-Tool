import tkinter as tk
import pyautogui
import time
import keyboard

# function to switch windows
def switch_to_program(program_title):
    windows = pyautogui.getAllTitles()
    target_window = None
    for window in windows:
        if program_title in window:
            target_window = window
            break
    if target_window:
        pyautogui.getWindowsWithTitle(target_window)[0].activate()

# function for the button that does everything
def button():
    # switches to LOL
    switch_to_program('League of Legends')
    # gets text from text box
    text = display.get("1.0", tk.END).replace('\n', ' ')
    while True:
        # checks if f1 is being pressed to stop program
        if keyboard.is_pressed('f1'):
            break
        # types stuff in based on character count
        if len(text) > 115:
            chunk = text[0:115]
            keyboard.press('enter')
            keyboard.release('enter')
            time.sleep(0.8)
            for x in chunk:
                keyboard.write(x)
                time.sleep(0.05)
            keyboard.press('enter')
            keyboard.release('enter')
            time.sleep(1)
            text = text[115:]
        else:
            keyboard.press('enter')
            keyboard.release('enter')
            time.sleep(0.8)
            for x in text:
                keyboard.write(x)
                time.sleep(0.05)
            keyboard.press('enter')
            keyboard.release('enter')
            break

if __name__ == '__main__':
    root = tk.Tk()
    # make title in the program
    root.title('League Chat Copy Paste Tool')
    # set screen size
    root.geometry('800x900')
    # try to put program in middle of screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width - root.winfo_reqwidth()) // 2) - round(screen_width * 0.16)
    y = ((screen_height - root.winfo_reqheight()) // 2) - round(screen_height * 0.32)
    root.geometry('+{}+{}'.format(x, y))
    # add a title in the program
    title_font = ('Helvetica', 18, 'bold')
    title_label = tk.Label(root, text='Paste Message Here!!!', font=title_font)
    title_label.pack(pady=10)
    # adds info text
    info_font = ('Helvetica', 8, 'bold')
    info_label = tk.Label(root, text='Hold f1 to stop', font=info_font)
    info_label.pack()
    # adds a text box
    display = tk.Text(root, height=30, width=50, wrap=tk.WORD)
    display.pack(pady=15)
    # add a button for the copy-paste
    button = tk.Button(root, text="Paste", command=button, width=40, height=5, font=('Helvetica', 14))
    button.pack(pady=3, anchor='center', side='top')
    # runs everything
    root.mainloop()
