from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

window = Tk()
window.title("MNIST Test")

image_label = Label()
image_label.grid(row=0, column=0)


def button_click():
    file = filedialog.askopenfile(mode="r", filetypes=[("PNG Images", "*.png")])
    img = ImageTk.PhotoImage(Image.open(file.name))
    image_label.image = img
    image_label.configure(image=img)


button1 = Button(window, text="Load image", command=button_click)
button1.grid(row=1, column=0)

window.mainloop()
