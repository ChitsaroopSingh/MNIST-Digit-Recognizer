import tkinter as tk
from PIL import Image, ImageDraw

WIDTH = 280
HEIGHT = 280

root = tk.Tk()
root.title("Draw a digit")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

image = Image.new("L", (WIDTH, HEIGHT), 255)
draw = ImageDraw.Draw(image)

def paint(event):
    r = 10

    x1 = event.x - r
    y1 = event.y - r
    x2 = event.x + r
    y2 = event.y + r

    canvas.create_oval(x1, y1, x2 , y2,
                       fill="white", outline="white")
    draw.ellipse([x1, y1, x2 , y2], fill=0)

canvas.bind("<B1-Motion>", paint)

def save_image():
    small = image.resize((28, 28))
    small.save("digit28.png")
    print("Saved!")

save_button = tk.Button(root, text="Save", command=save_image)
save_button.pack()

root.mainloop()