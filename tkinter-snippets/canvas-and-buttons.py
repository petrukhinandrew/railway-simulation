import tkinter

def func():
    print("Clicked")

# GUI window object
top = tkinter.Tk()

# Canvas object
C = tkinter.Canvas(top, bg="black", height=312, width=778)

# Specifying the coords of the keyboard
# Coords borders:
# y => 0-74, 76-160, 162-236, 238-312
# x => 0-50, 52-102, 104-154, 156-206,
# 208-258, 260-310, 312-362, 364-414,
# 416-466, 468-518, 520-570, 572-622,
# 624-674, 676-726, 728-778
y = (312,238,236,162,160,76,74,0)
x = (0,50,52,102,104,154,156,206,208,258,260,310,312,362,364,414,416,466,468,518,520,570,572,622,624,674,676,726,728,778)
by = (285, 199, 123, 37)
bx = (25,77,129,181,233,285,337,389,441,493,545,597,649,701,753)

yi = (0,2,4,6)
xi = (0,2,4,6,8,10,12,14,16,18,20,22,24,26,28)
biy = (0,1,2,3)
bix = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)

for indexY in yi:
    for indexX in xi:
        #print ("Xi = " + str(x[indexX]) + " Xi+1 = " + str(x[indexX+1]) + " Yi = " + str(y[indexY]) + " Yi+1 = " + str(y[indexY+1]))
        coord = x[ indexX ], y[ indexY ], x[ indexX ], y[ indexY + 1 ], x[ indexX + 1 ], y[ indexY + 1 ], x[ indexX + 1 ], y[ indexY ]
        # Create polygon object
        oval = C.create_polygon(coord, fill="white")

for indexY in biy:
    for indexX in bix:
        #print (by[indexY])
        #print (bx[indexX])
        B = tkinter.Button(top, text = 'A', command = func)
        B1 = C.create_window(bx[ indexX ] , by[ indexY ], window = B)

# Combine all canvas objects
C.pack()

# Combine all button objects
B.pack()

# Runs an infinite loop so that the resultant window doesn't disappear
# Executed only once when application is ready

top.mainloop()