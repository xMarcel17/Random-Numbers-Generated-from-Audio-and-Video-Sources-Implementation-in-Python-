import cv2
import numpy as np

def calculateColor(px):
    return px[2] << 16 + px[1] << 8 + px[0]

def calculateColorI(x,y,px):
    return (
        calculateColor(px[x-1][y-1])+calculateColor(px[x-1][y])+calculateColor(px[x-1][y+1])+
        calculateColor(px[x][y-1])+calculateColor(px[x][y])+calculateColor(px[x][y+1])+
        calculateColor(px[x+1][y-1])+calculateColor(px[x+1][y])+calculateColor(px[x+1][y+1])
    )/9

filename = 'Kanye_West_-_Gotcha.mp4'
#
vc = cv2.VideoCapture(filename)
c = 1
# wymiary obrazu
W = 640
H = 356
# vt i th
img = cv2.imread("frames/90.jpg")

vt = np.var(img)/2
th = 100
# zmienne initial value
R,G,B = 0,0,0
R1,G1,B1 = 0,0,0
R2,G2,B2 = 0,0,0

if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False

# rozmiar 640x356       indeksowanie pikseli od 0

# a----------------------------------------------------------------
img = cv2.imread("frames/"+str(c)+".jpg")
xc = int(W/2)
yc = int(H/2)

px = img[xc][yc]

color = calculateColorI(xc,yc,px)

x = (color)%(W/2)+(W/4)
y = (color)%(H/2)+(H/4)

# b----------------------------------------------------------------
watchdog = 0

# c----------------------------------------------------------------

while rval:
    rval, frame = vc.read()     # wcztanie klatki z wideo (wizji)
    # obliczenie initial value 

    
    # cv2.imwrite('frames/'+str(c) + '.jpg',frame)
    # c = c + 1
    # print(c)
    cv2.waitKey(1)
vc.release()