import cv2
import numpy as np

def calculateColor(px):
    ret = px[2]
    ret = ret << 8
    ret += px[1]
    ret = ret << 8
    ret += px[0]
    return ret

def calculateColorI(x,y,px):
    if(x == 0): # dodalem to zeby nie bylo bledow ze zczytuje kolor z poza obrazka
        x += 1  # narazie zostawiam, zobaczymy czy dziala
    if(x == 639): # dziala
        x -= 1
    if(y == 0):
        y += 1
    if(y == 355):
        y -= 1
    return (
        calculateColor(px[y-1][x-1])+calculateColor(px[y][x-1])+calculateColor(px[y+1][x-1])+
        calculateColor(px[y-1][x])+calculateColor(px[y][x])+calculateColor(px[y+1][x])+
        calculateColor(px[y-1][x+1])+calculateColor(px[y][x+1])+calculateColor(px[y+1][x+1])
    )/9

randomBits = []
filename = 'Kanye_West_-_Gotcha'
#
vc = cv2.VideoCapture(filename+'.mp4')
audio = open(filename+'.wav', 'rb')
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
state = 0
audio_content = bytearray(audio.read())
ranBitCnt=0
i = 0  # i = 0-7
runcnt = 0
K = 500
x = int(W/2)
y = int(H/2)

while c<=90:
    #print(c)
    img = cv2.imread("frames/"+str(c)+".jpg")
    if(state == 0):
        #print("Stan 0")
        # a----------------------------------------------------------------
        px = img[y][x]

        R = px[2]
        G = px[1]
        B = px[0]

        color = calculateColorI(x,y,img)
        x = round((color)%(W/2)+(W/4))
        y = round((color)%(H/2)+(H/4))
        # b----------------------------------------------------------------
        watchdog = 0
        state = 1
    elif(state == 1):
        #print("Stan 1")
        # d----------------------------------------------------------------
        while (watchdog <= th):
            diff = (R-R1)**2 + (G-G1)**2 + (B-B1)**2

            if(diff < vt):
                x = (x + (R ^ G) + 1) % W
                y = (y + (G ^ B) + 1) % H
                px = img[y][x]
                watchdog+=1
                continue
            state = 2
            break  
        if(watchdog > th):
            state = 0
    elif(state == 2):
        #print("Stan 2")
        # c----------------------------------------------------------------

        n1 = (10 + (R*i + (G << 2) + B + runcnt)%(K/2))
        n2 = (15 + (R*i + (G << 3) + B + runcnt)%(K/2))
        n3 = (20 + (R*i + (G << 4) + B + runcnt)%(K/2))
        n4 = (5 + (R*i + (G << 1) + B + runcnt)%(K/2))
        n5 = (25 + (R*i + (G << 5) + B + runcnt)%(K/2))

        SN1 = audio_content[int(n1)] 
        SN2 = audio_content[int(n2)]
        SN3 = audio_content[int(n3)]
        SN4 = audio_content[int(n4)]
        SN5 = audio_content[int(n5)]
        state = 3
    elif(state == 3):
        #print("Stan 3")
        # e----------------------------------------------------------------
        ranBit = (1 & (R^G^B^R1^G1^B1^R2^G2^B2^SN1^SN2^SN3^SN4^SN5))
        randomBits.append(ranBit)
        ranBitCnt+=1
        i+=1
        R1 = R
        G1 = G
        B1 = B

        x = (((R^x) << 4)^(G^y))%W
        y = (((G^x) << 4)^(B^y))%H
        state = 2
        if(i==8):
            # g----------------------------------------------------------------
            R2 = R
            G2 = G
            B2 = B
            i = 0
            c += 1
            #print("wkraczamy")
            state = 0 
# f----------------------------------------------------------------

# while rval:
#     rval, frame = vc.read()     # wcztanie klatki z wideo (wizji)
#     # obliczenie initial value 

    
#     # cv2.imwrite('frames/'+str(c) + '.jpg',frame)
#     # c = c + 1
#     # print(c)
#     cv2.waitKey(1)
# vc.release()
l = 0
for i in randomBits:
    print("Bit numer "+str(l)+" = "+str(i))
    l += 1
audio.close()