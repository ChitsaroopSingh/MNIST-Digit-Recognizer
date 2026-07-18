import tkinter as tk
from PIL import Image, ImageDraw

WIDTH = 280
HEIGHT = 280

root = tk.Tk()
root.title("Draw a digit")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()