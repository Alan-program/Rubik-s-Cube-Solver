import cv2
import numpy as np
import colordetection as cd
import kociemba
#a dictionary of Lists(changeable)
#preview中的預覽白色方格
state=  {
            'up':['white','white','white','white','white','white','white','white','white',],
            'right':['white','white','white','white','white','white','white','white','white',],
            'front':['white','white','white','white','white','white','white','white','white',],
            'down':['white','white','white','white','white','white','white','white','white',],
            'left':['white','white','white','white','white','white','white','white','white',],
            'back':['white','white','white','white','white','white','white','white','white',]
        }
#將顏色轉成kociemba可讀的模式
sign_conv={
            'green'  : 'F',
            'white'  : 'U',
            'blue'   : 'B',
            'red'    : 'R',
            'orange' : 'L',
            'yellow' : 'D'
          }

color = {
        'red'    : (0,0,255),
        'orange' : (0,165,255),
        'blue'   : (255,0,0),
        'green'  : (0,255,0),
        'white'  : (255,255,255),
        'yellow' : (0,255,255)
        }

#a dictionary of 9*2 Lists(changeable)
stickers = {
        'main': [
            [200, 120], [300, 120], [400, 120],
            [200, 220], [300, 220], [400, 220],
            [200, 320], [300, 320], [400, 320]
        ],
        'current': [
            [20, 20], [54, 20], [88, 20],
            [20, 54], [54, 54], [88, 54],
            [20, 88], [54, 88], [88, 88]
        ],
        'preview': [
            [20, 130], [54, 130], [88, 130],
            [20, 164], [54, 164], [88, 164],
            [20, 198], [54, 198], [88, 198]
        ],
        'left': [
            [50, 280], [94, 280], [138, 280],
            [50, 324], [94, 324], [138, 324],
            [50, 368], [94, 368], [138, 368]
        ],
        'front': [
            [188, 280], [232, 280], [276, 280],
            [188, 324], [232, 324], [276, 324],
            [188, 368], [232, 368], [276, 368]
        ],
        'right': [
            [326, 280], [370, 280], [414, 280],
            [326, 324], [370, 324], [414, 324],
            [326, 368], [370, 368], [414, 368]
        ],
        'up': [
            [188, 128], [232, 128], [276, 128],
            [188, 172], [232, 172], [276, 172],
            [188, 216], [232, 216], [276, 216]
        ],
        'down': [
            [188, 434], [232, 434], [276, 434],
            [188, 478], [232, 478], [276, 478],
            [188, 522], [232, 522], [276, 522]
        ], 
        'back': [
            [464, 280], [508, 280], [552, 280],
            [464, 324], [508, 324], [552, 324],
            [464, 368], [508, 368], [552, 368]
        ],
           }
font = cv2.FONT_HERSHEY_SIMPLEX
#a dictionary
textPoints=  {
            'up':[['U',242, 202],['W',(255,255,255),260,208]],
            'right':[['R',380, 354],['R',(0,0,255),398,360]],
            'front':[['F',242, 354],['G',(0,255,0),260,360]],
            'down':[['D',242, 508],['Y',(0,255,255),260,514]],
            'left':[['L',104,354],['O',(0,165,255),122,360]],
            'back':[['B',518, 354],['B',(255,0,0),536,360]],
        }

#ColorDetection中的白色方格
def draw_stickers(frame,stickers,name): #30px*30px retangle stickers with 2px black outline
        for x,y in stickers[name]:
            cv2.rectangle(frame, (x,y), (x+30, y+30), (255,255,255), 2)

#Preview中的結果方格
def draw_preview_stickers(frame,stickers):
        stick=['front','back','left','right','up','down']
        for name in stick:
            for x,y in stickers[name]:
                cv2.rectangle(frame, (x,y), (x+40, y+40), (255,255,255), 2)

#Preview的結果方格中的文字及顏色(eg.U,D,F)
def texton_preview_stickers(frame,stickers):
        stick=['front','back','left','right','up','down']
        for name in stick:
            for x,y in stickers[name]:
                sym,x,y=textPoints[name][0][0],textPoints[name][0][1],textPoints[name][0][2]
                cv2.putText(frame, sym, (x,y), font,1,(0, 0, 0), 1, cv2.LINE_AA)  
                sym,col,x,y=textPoints[name][1][0],textPoints[name][1][1],textPoints[name][1][2],textPoints[name][1][3]             
                cv2.putText(frame, sym, (x,y), font,0.5,col, 1, cv2.LINE_AA) 

#填滿preview中的白色方格顏色
def fill_stickers(frame,stickers,sides):    
    for side,colors in sides.items():
        num=0
        for x,y in stickers[side]:
            cv2.rectangle(frame,(x,y),(x+40,y+40),color[colors[num]],-1)
            num+=1

#利用kociemba得到解法
def solve(state):
    raw=''
    for i in state:
        for j in state[i]:
            raw+=sign_conv[j]
    print("answer:",kociemba.solve(raw))
    return kociemba.solve(raw)

check_state=[]
cap = cv2.VideoCapture(0)
if __name__=='__main__':
    #繪製一個600px*700px的黑色畫布
    preview = np.zeros((600,700,3), np.uint8) #np.uint8 represent the range of [0,255]
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        bgr=[] #declare rgb
        current_state=[] #declare current_state
        ret, img = cap.read()             # 讀取影片的每一幀
        mask = np.zeros(img.shape, dtype=np.uint8)
        if not ret: #ret表示是否讀取順利(T or F)
            print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
            break
        draw_stickers(img,stickers,'main') #Color Detection中的辨識方塊
        draw_stickers(img,stickers,'current') #Color Detection中的辨識結果
        draw_preview_stickers(preview,stickers) #Preview中的結果方格
        fill_stickers(preview,stickers,state) #填滿preview中的白色方格顏色
        texton_preview_stickers(preview,stickers) #Preview的結果方格中的文字及顏色(eg.U,D,F)

        for i in range(9):
            bgr.append(img[stickers['main'][i][1]+10][stickers['main'][i][0]+10])

        a=0
        for x,y in stickers['current']:
            color_name=cd.color_detect(bgr[a][0],bgr[a][1],bgr[a][2])
            cv2.rectangle(img,(x,y),(x+30,y+30),color[color_name],-1)
            a+=1
            current_state.append(color_name)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        elif k ==ord('u'):
            state['up']=current_state
            check_state.append('u')
        elif k ==ord('r'):
            check_state.append('r')
            state['right']=current_state
        elif k ==ord('l'):
            check_state.append('l')
            state['left']=current_state
        elif k ==ord('d'):
            check_state.append('d')
            state['down']=current_state       
        elif k ==ord('f'):
            check_state.append('f')
            state['front']=current_state       
        elif k ==ord('b'):
            check_state.append('b')
            state['back']=current_state       

        if len(set(check_state))==6:
            solved=solve(state)

        cv2.imshow('Preview',preview)
        cv2.imshow('ColorDetection', img[0:500,0:500]) #如果讀取成功，顯示Color Detection的畫面(500*500)
    cap.release()                           # 所有作業都完成後，釋放資源
cv2.destroyAllWindows() 

