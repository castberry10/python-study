from tkinter import *

board = [[0,0,0],[0,0,0],[0,0,0]]

def runCanvas(canvas_width, canvas_height):
    master = Tk()
    master.resizable(width=False, height=False)
    canvas = Canvas(master, width=canvas_width, height=canvas_height)
    canvas.pack()

    drawBoard(canvas)
    startGame(canvas)

    master.mainloop()

def printBoard():
    for i in range(3):
        print(board[i])
    print()


def interpolate(t, c1, c2):
    return int((1 - t) * c1[0] + t * c2[0]), int((1 - t) * c1[1] + t * c2[1]), int((1 - t) * c1[2] + t * c2[2])

def rgbString(rgb):
    return "#%02x%02x%02x" % (rgb[0], rgb[1], rgb[2])

def drawCircle(canvas,a, b,color):
    if a==0 & b==0:
        canvas.create_oval(0, 0, 100, 100, fill=color)
    elif a==0 & b==1:
        canvas.create_oval(100, 0, 200, 100, fill=color)
    elif a == 0 & b == 2:
        canvas.create_oval(200, 0, 300, 100, fill=color)
    elif a == 1 & b == 0:
        canvas.create_oval(0, 100, 100, 200, fill=color)
    elif a == 1 & b == 1:
        canvas.create_oval(100, 100, 200, 200, fill=color)
    elif a == 1 & b == 2:
        canvas.create_oval(200, 100, 300, 200, fill=color)
    elif a == 2 & b==0:
        canvas.create_oval(0, 200, 100, 300, fill=color)
    elif a==2 & b==1:
        canvas.create_oval(100, 200, 200, 300, fill=color)
    elif a==2 & b==2:
        canvas.create_oval(200, 200, 300, 300, fill=color)

def drawBoard(canvas):
    canvas.create_line(0, 100, 300, 100)
    canvas.create_line(0, 200, 300, 200)
    canvas.create_line(0, 300, 300, 300)
    canvas.create_line(100, 0, 100, 300)
    canvas.create_line(200, 0, 200, 300)
    canvas.create_line(300, 0, 300, 300)

def startGame(canvas):
    yellowRGB = (255, 255, 0)
    redRGB = 255, 0, 0
    mixedRGB = interpolate(0.5, yellowRGB, redRGB)
    mixed = rgbString(mixedRGB)
    printBoard()
    ox = 1
    cnt = 0
    color = "red"

    for i in range(10):
        a, b = input("input : ").split()
        a = int(a)
        b = int(b)


        if board[a][b] == 0:
            board[a][b] = ox
            cnt += 1
            drawCircle(canvas, a, b, color)
            printBoard()
        else :
            print("Already Chosen\n")
            continue

        if cnt >= 5:
            if board[0][0] == board[0][1] == board[0][2] != 0 :
                print("\n\nEnd")
                canvas.create_polygon(0, 300, 300, 500, fill=color)
                break
            elif board[1][0] == board[1][1] == board[1][2] != 0 :
                print("\n\nEnd")
                canvas.create_polygon(0, 300, 300, 500, fill=color)
                break
            elif board[2][0] == board[2][1] == board[2][2] != 0 :
                print("\n\nEnd")
                canvas.create_polygon(0, 300, 300, 500, fill=color)
                break
            elif board[0][0] == board[1][0] == board[2][0] != 0 :
                print("\n\nEnd")
                canvas.create_polygon(0, 300, 300, 500, fill=color)
                break
            elif board[0][1] == board[1][1] == board[2][1] != 0 :
                print("\n\nEnd")
                canvas.create_polygon(0, 300, 300, 500, fill=color)
                break
            elif board[0][2] == board[1][2] == board[2][2] != 0 :
                print("\n\nEnd")
                canvas.create_polygon(0, 300, 300, 500, fill=color)
                break
            elif board[0][0] == board[1][1] == board[2][2] != 0:
                print("\n\n\nEnd")
                canvas.create_polygon(0, 300, 300, 500, fill=color)
                break
            elif board[0][2] == board[1][1] == board[2][0] != 0 :
                print("\n\nEnd")
                canvas.create_polygon(0, 300, 300, 500, fill=color)
                break

        if ox == 1:
            ox = -1
        else:
            ox = 1

        if color == "red":
            color = "yellow"
        else:
            color = "red"

        if cnt == 9:
            print("\n\nDraw")
            canvas.create_polygon(0, 300, 300, 400, fill=mixed)
            break



runCanvas(300, 400)