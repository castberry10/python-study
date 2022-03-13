from tkinter import *
import math

def drawLine(cavars, width, height):
    cavars.create_line(0, height / 5, width, height / 5)
    cavars.create_line(0, height * 2 / 5, width, height * 2 / 5)
    cavars.create_line(0, height * 3 / 5, width, height * 3 / 5)
    cavars.create_line(width / 3, 0, width / 3, height * 3 / 5)
    cavars.create_line(width * 2 / 3, 0, width * 2 / 3, height * 3 / 5)

def drawCircle(cavars, width, height, num, man):
    if man > 0:
        color = "yellow"
    elif man < 0:
        color = "red"

    if num[0] == 0:
        if num[1] == 0:
            cavars.create_oval(0, 0, 100, 100, fill=color)
        elif num[1] == 1:
            cavars.create_oval(100, 0, 200, 100, fill=color)
        elif num[1] == 2:
            cavars.create_oval(200, 0, 300, 100, fill=color)

    elif num[0] == 1:
        if num[1] == 0:
            cavars.create_oval(0, 100, 100, 200, fill=color)
        elif num[1] == 1:
            cavars.create_oval(100, 100, 200, 200, fill=color)
        elif num[1] == 2:
            cavars.create_oval(200, 100, 300, 200, fill=color)
    elif num[0] == 2:
        if num[1] == 0:
            cavars.create_oval(0, 200, 100, 300, fill=color)
        elif num[1] == 1:
            cavars.create_oval(100, 200, 200, 300, fill=color)
        elif num[1] == 2:
            cavars.create_oval(200, 200, 300, 300, fill=color)




def runCanvas(canvas_width, canvas_height):
    master = Tk()
    master.resizable(width=False, height=False)
    canvas = Canvas(master, width=canvas_width, height=canvas_height)
    canvas.pack()
    drawCanvas(canvas, canvas_width, canvas_height)
    cnt = 1
    man = 1
    x, y = 0,0
    ttt = [[0,0,0],[0,0,0],[0,0,0]]
    while True:
        if cnt > 9:
            canvas.create_polygon(canvas_width/2,canvas_height*3/5, 0, canvas_height*4/5, canvas_width/2, canvas_height, canvas_width, canvas_height*4/5, fill='#ff7f00')
            canvas.create_text(canvas_width / 2, canvas_height * 4/ 5, text="Draw")
            break
        else: # 안끝났다면
            color = ''
            if cnt % 2 == 1:
                man = 1
                color = 'yellow'
            else:
                man = -1
                color = 'red'
            master.update()

            x, y = input("input : ").split()
            print("")
            x = int(x)
            y = int(y)

            if ttt[x][y] == 0:
                drawCircle(canvas, canvas_width, canvas_height, (x, y), man)
                master.update()
                ttt[x][y] = man
                cnt += 1
                for i in range(3):
                        print(ttt[i])
                print()

            elif ttt[x][y] != 0:
                print("다시 입력")
                continue

            if ttt[0][0] == ttt[0][1] == ttt[0][2] != 0:
                canvas.create_polygon(canvas_width / 2, canvas_height * 3 / 5, 0, canvas_height * 4 / 5,
                                      canvas_width / 2, canvas_height, canvas_width, canvas_height * 4 / 5,
                                      fill=color)
                canvas.create_text(canvas_width / 2, canvas_height * 4/ 5, text="Win")
                print("End")
                break
            elif ttt[1][0] == ttt[1][1] == ttt[1][2] != 0:
                canvas.create_polygon(canvas_width / 2, canvas_height * 3 / 5, 0, canvas_height * 4 / 5,
                                      canvas_width / 2, canvas_height, canvas_width, canvas_height * 4 / 5,
                                      fill=color)
                canvas.create_text(canvas_width / 2, canvas_height * 4/ 5, text="Win")
                print("End")
                break
            elif ttt[2][0] == ttt[2][1] == ttt[2][2] != 0:
                canvas.create_polygon(canvas_width / 2, canvas_height * 3 / 5, 0, canvas_height * 4 / 5,
                                      canvas_width / 2, canvas_height, canvas_width, canvas_height * 4 / 5,
                                      fill=color)
                canvas.create_text(canvas_width / 2, canvas_height * 4/ 5, text="Win")
                print("End")
                break
            elif ttt[0][0] == ttt[1][1] == ttt[2][2] != 0:
                canvas.create_polygon(canvas_width / 2, canvas_height * 3 / 5, 0, canvas_height * 4 / 5,
                                      canvas_width / 2, canvas_height, canvas_width, canvas_height * 4 / 5,
                                      fill=color)
                canvas.create_text(canvas_width / 2, canvas_height * 4/ 5, text="Win")
                print("End")
                break
            elif ttt[2][0] == ttt[1][1] == ttt[0][2] != 0:
                canvas.create_polygon(canvas_width / 2, canvas_height * 3 / 5, 0, canvas_height * 4 / 5,
                                      canvas_width / 2, canvas_height, canvas_width, canvas_height * 4 / 5,
                                      fill=color)
                canvas.create_text(canvas_width / 2, canvas_height * 4/ 5, text="Win")
                print("End")
                break
            elif ttt[0][0] == ttt[1][0] == ttt[2][0] != 0:
                canvas.create_polygon(canvas_width / 2, canvas_height * 3 / 5, 0, canvas_height * 4 / 5,
                                      canvas_width / 2, canvas_height, canvas_width, canvas_height * 4 / 5,
                                      fill=color)
                canvas.create_text(canvas_width / 2, canvas_height * 4/ 5, text="Win")
                print("End")
                break
            elif ttt[0][1] == ttt[1][1] == ttt[2][1] != 0:
                canvas.create_polygon(canvas_width / 2, canvas_height * 3 / 5, 0, canvas_height * 4 / 5,
                                      canvas_width / 2, canvas_height, canvas_width, canvas_height * 4 / 5,
                                      fill=color)
                canvas.create_text(canvas_width / 2, canvas_height * 4/ 5, text="Win")
                print("End")
                break
            elif ttt[0][2] == ttt[1][2] == ttt[2][2] != 0:
                canvas.create_polygon(canvas_width / 2, canvas_height * 3 / 5, 0, canvas_height * 4 / 5,
                                      canvas_width / 2, canvas_height, canvas_width, canvas_height * 4 / 5,
                                      fill=color)
                canvas.create_text(canvas_width / 2, canvas_height * 4/ 5, text="Win")
                print("End")
                break

    master.mainloop()

def drawCanvas(canvas, width, height):
    print("input ex.) 0 1 ")
    drawLine(canvas, width, height)

r2unCanvas(300, 500)
1