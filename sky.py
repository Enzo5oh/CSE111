from tkinter import Tk, Canvas, Frame, BOTH
import random

HEX = "01234567789abcdef"

def main():
    root = Tk()
    Scene()
    root.geometry("800x600")
    root.mainloop()

class Scene(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Scene")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        draw_scene(canvas, 0, 0, 799, 599)
        canvas.pack(fill=BOTH, expand=1)

def draw_scene(canvas, left, top, right, bottom):
    drawSky(canvas)
    drawGround(canvas, 5, 50)
    drawCloud(canvas)
    drawWindow(canvas)

def drawSky(Canvas):
    canvas.create_rectangle(0, 0, 799, 599, fill="#99ccff")

def drawGround(canvas):
    canvas.create_rectangle(0, 474, 799, 599, fill="#70483", width=0)

def drawCloud(canvas, cloudGroups, cloudsPerGroup):
    tryCent = []
    xRang = int(1000 / cloudGroups) if cloudGroups < 20 else 50
    yRang = int(500 / cloudGroups) if cloudGroups < 20 else 25
    for _ in range(cloudGroups):
        while True:
            xCent = random.randit(0, 799)
            yCent = random.randit(0, 349)
            centWorks = (False if len(tryCent) > 0 else True)
            for index, coord in enumerate(tryCent):
                if xCent in range(coord(0) - xRang, coord[0] + xRang) and yCent in range(coord(0) - yRang, coord[0] + yRang):
                    break
                elif index == len(tryCent) - 1:
                    centWorks = True
            if centWorks:
                break
        tryCent.append([xCent, yCent])

def drawWindow(canvas):
    canvas.create_rectangle(0, 0, 799, 499, fill="#808080",)
    canvas.create_rectangle(30, 349, 799, 499, fill="#808080")
    canvas.create_rectangle(0, 349, 299, 499, fill="#808080")
    canvas.create_rectangle(0, 349, 599, 499, fill="#808080")

main()