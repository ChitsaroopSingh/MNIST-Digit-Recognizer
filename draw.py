import tkinter as tk
import numpy as np
from PIL import Image, ImageDraw

WIDTH = 280
HEIGHT = 280

def draw_digit():
    root = tk.Tk()
    root.title("Draw a digit")

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
    canvas.pack()

    image = Image.new("L", (WIDTH, HEIGHT), 0)
    draw = ImageDraw.Draw(image)

    def paint(event):
        r = 10

        x1 = event.x - r
        y1 = event.y - r
        x2 = event.x + r
        y2 = event.y + r

        canvas.create_oval(x1, y1, x2 , y2,
                        fill="white", outline="white")
        draw.ellipse([x1, y1, x2 , y2], fill=255)

    canvas.bind("<B1-Motion>", paint)

    digit = None
    def save_image():
        nonlocal digit
        small = image.resize((28, 28) , Image.Resampling.LANCZOS)
        small.save("digit28.png")

        digit = np.array(small)
        digit = digit.reshape(1, 784)

        root.destroy()
        
        return digit
        
    save_button = tk.Button(root, text="Save", command=save_image)
    save_button.pack()

    root.mainloop()

    return digit

