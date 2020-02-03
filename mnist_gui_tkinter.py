from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense

# Load neural network
model = load_model(filepath='mnist-100b-relu-chkpt-83-0.98988.h5')

# Define UI elements
window = Tk()
window.title('MNIST Test')

image_label = Label()
image_label.grid(row=0, column=0)

label2 = Label(text='Prediction: ')
label2.grid(row=0, column=1)
label_predict = Label(text='X')
label_predict.grid(row=0, column=2)
label3 = Label(text='Rounded: ')
label3.grid(row=1, column=1)
label_rounded = Label(text='X')
label_rounded.grid(row=1, column=2)


def button_click():
    file = filedialog.askopenfile(mode='r', filetypes=[('PNG Images', '*.png')])
    img = Image.open(file.name)
    photo_img = ImageTk.PhotoImage(img)
    image_label.image = photo_img
    image_label.configure(image=photo_img)
    data = np.array(img.getdata()).reshape((1, 28 * 28))
    predictions = model.predict(data)
    label_predict = Label(text=predictions)
    label_predict.grid(row=0, column=2)
    label_rounded = Label(text=round(predictions[0][0], ndigits=0))
    label_rounded.grid(row=1, column=2)


button1 = Button(window, text='Load image', command=button_click)
button1.grid(row=1, column=0)

window.mainloop()
