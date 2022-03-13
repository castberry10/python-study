from tkinter import *

TTT = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
master = Tk()
master.resizable(width=False, height=False)
canvas = Canvas(master, width=200, height=300)

def draw(canvas, width, height):
    for i in range(1, 4):
        canvas.create_line(0, height / 3 * i, width, height / 3 * i)
        canvas.create_line(width / 3 * i, 0, width / 3 * i, height)


def runCanvas(canvas_width, canvas_height):
    canvas.pack()
    draw(canvas, 200, 200)


def drawCircle(canvas, width, height, i, j, key):
    r = min(width, height) / 3 / 2
    c = (width / 3 * (j + 1) - r, height / 3 * (i + 1) - r)

    if key == 1:
        canvas.create_oval(c[0] - r, c[1] - r, c[0] + r, c[1] + r, fill="yellow")
    elif key == -1:
        canvas.create_oval(c[0] - r, c[1] - r, c[0] + r, c[1] + r, fill="red")


def check(List):
    for i in range(3):
        if List[i][0] == List[i][1] == List[i][2] != 0:
            return List[i][0]
        elif List[0][i] == List[1][i] == List[2][i] != 0:
            return List[0][i]
        elif List[0][0] == List[1][1] == List[2][2] != 0:
            return List[0][0]
        elif List[0][2] == List[1][1] == List[2][0] != 0:
            return List[0][0]

    return 0


def game():
    runCanvas(300, 300)
    key = 1
    end = 0

    for i in range(9):
        print(TTT[0])
        print(TTT[1])
        print(TTT[2])
        print()

        while True:
            master.update()
            string = input("input: ")
            x = int(string[0])
            y = int(string[2])
            if x < 0 or y < 0 or x > 2 or y > 2:
                print("Input 0~2")
                continue
            if TTT[x][y] == 0:
                TTT[x][y] = key
                drawCircle(canvas, 200, 200, x, y, TTT[x][y])
                break
            else:
                print("Already Chosen")

        result = check(TTT)
        if result != 0:
            print("End")
            if result == 1:
                canvas.create_polygon(0, 250, 100, 300, 200, 250, 100, 200, fill="yellow")
            else:
                canvas.create_polygon(0, 250, 100, 300, 200, 250, 100, 200, fill="red")
            canvas.create_text(100, 250, text="Win")
            end = 1
            master.mainloop()
            break

        key *= -1

    if end == 0:
        print(TTT[0])
        print(TTT[1])
        print(TTT[2])
        print("Draw")
        canvas.create_polygon(0, 250, 100, 300, 200, 250, 100, 200, fill="orange")
        canvas.create_text(100, 250, text="Draw")
        master.mainloop()


game()
