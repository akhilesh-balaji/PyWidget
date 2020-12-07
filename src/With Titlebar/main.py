import tkinter
import tkinter.messagebox
import tkinter.ttk
import pygetwindow as gw  # Install dependency with `pip install pygetwindow`
from random import randint


# Defining Window Properties
root = tkinter.Tk()
root.withdraw()


def getPos(event):
    """Get the position of the window"""

    xwin = window.winfo_x()
    ywin = window.winfo_y()
    startx = event.x_root
    starty = event.y_root

    ywin = ywin - starty
    xwin = xwin - startx

    def moveWindow(event):
        """Moving the window on mouse move"""

        window.geometry(
            "310x310" + f'+{event.x_root + xwin}+{event.y_root + ywin}')

    startx = event.x_root
    starty = event.y_root

    titleBar.bind('<B1-Motion>', moveWindow)


def topOrNot():
    """
    Detects wheather the window should be shown or not.

    Makes it act like a Desktop widget.
    """

    # TODO: Refine this logic
    # HELP WANTED

    windows = gw.getActiveWindow()

    # Desktop Widget logic
    if windows is None:
        window.deiconify()
        window.lift()
        window.attributes("-topmost", True)
    else:
        if windows.isMaximized:
            window.lower()
            window.attributes("-topmost", False)
        elif (not windows.isMaximized and windows.title != "" and
                windows.title != "Widget"):
            window.deiconify()
            window.attributes("-topmost", False)
            window.lower()
        elif (not windows.isMaximized and windows.title != "" and
                windows.title == "Widget"):
            window.attributes("-topmost", False)
        elif windows.title == "tk":
            window.deiconify()
            window.lift()
            window.attributes("-topmost", True)
        else:
            window.deiconify()
            window.lift()
            window.attributes("-topmost", True)

    window.after(10, topOrNot)


window = tkinter.Toplevel()
window.title("Widget")
window.attributes("-toolwindow", True)
window.overrideredirect(1)
window.config(bg="white")
window.geometry("310x310+" + str(randint(10, 900)) +
                "+" + str(randint(10, 500)))
window.wait_visibility(window)

# Configuring grid
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=100000)
window.grid_columnconfigure(3, weight=1000)
window.grid_columnconfigure(4, weight=0)
window.grid_columnconfigure(5, weight=0)
window.grid_columnconfigure(6, weight=0)

# Defining Title Bar Elements
titleBar = tkinter.Frame(window, relief="flat")
titleBar.pack()

dummy2 = tkinter.Button(
    # Put in whatever you want in the titlebar
    titleBar,
    text=" ",
    padx=3,
    bd=0,
    bg="#F2F2F2",
    command=None)
dummy2.grid(row=0, column=0, padx=3, sticky="W")

dummy = tkinter.Button(
    # Put in whatever you want in the titlebar
    titleBar,
    text="🗕 🗖 ✕",
    bd=0,
    padx=3,
    bg="#F2F2F2",
    command=None)
dummy.grid(row=0, column=6, padx=220,  # Update padx depending on window size
           sticky="E")


# Widget Contents
dummyFrame = tkinter.Frame(
    window,
    relief="flat",
    bg="white",
    height=200,
    width=297)
dummyFrame.pack()

dummyContent = tkinter.Label(
    dummyFrame,
    font="Segoe_UI 11",
    padx=5,
    pady=10,
    bd=0,
    fg="black",
    relief="flat",
    height=10,
    width=36)
dummyContent.pack()

window.after(10, topOrNot())

titleBar.bind("<Button-1>", getPos)

window.mainloop()
