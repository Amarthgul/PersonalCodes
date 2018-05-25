'''
The goal is to creat a script that read a video file
Play it and allow users to capture and save certain frames

Current progress: |##################  | 90% Never Ending Story
'''


import cv2
import numpy as np

index = 0

def inspectAndCap(fileName, grayScale = False):  

    cap = cv2.VideoCapture(fileName)
    totalFrame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    #print(totalFrame)
    
    global index
    showInstructions = False
    recording = False
    ret, sample = cap.read()
    height, width, channels = sample.shape
    rectLoc_1 = (height//16 ,width//20)
    rectLoc_2 = (width//2, height//8)
    textLoc = (height//15 ,width//15)
    instructions = ['Right Arrow Key: Next Frame',
                    'Left Arrow Key: Last Frame',
                    'S: Start Recording Frames',
                    'R: Record Current Frame',
                    'Q: Quit']

    def selectZone(event, x, y, flags, param):
        global index
        if event == cv2.EVENT_LBUTTONDOWN:
            clickLoc = [x, y]
            index = int(totalFrame * (clickLoc[0] / width))
            cap.set(1, index)
            ret, frame = cap.read() 
            current = frame
            cv2.imshow('frame', current)

    while(True):
        
        cap.set(1, index)
        ret, frame = cap.read()
        current = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) if grayScale else frame

        

        #Left: 2424832 Up: 2490368 Right: 2555904 Down: 2621440
        key = cv2.waitKeyEx(0)
        if key == 2555904: index += 1
        elif key == 2424832: index -= 1
        elif key == ord('q'): break
        elif key == ord('i'): showInstructions = ~showInstructions
        elif key == ord('r') and not recording: cv2.imwrite('frame{}.png'.format(index), frame)
        elif key == ord('s'): recording = ~recording

        if recording: cv2.imwrite('frame{}.png'.format(index), frame)

        cv2.rectangle(current, rectLoc_1, rectLoc_2, (0,0,0) ,50)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(current,'frame {}, total second {}, recording: {}'.format(index, index//24, recording),
                    textLoc, font, 1, (255,255,255), 2, cv2.LINE_AA)
 
        if showInstructions:
            for i, text in zip(np.arange(1, len(instructions), 1), instructions):
                cv2.putText(current, text, 
                        (height//15, width//15 + i*width//30), font, 1, (255,255,255), 2, cv2.LINE_AA)

        cv2.line(current,(0, int(height*0.9)),
                 (width, int(height*0.9)), (0,0,0), 20)
        currentProgressPixel = int(width * (index / totalFrame))
        cv2.line(current, (currentProgressPixel, int(height*0.91)),
                 (currentProgressPixel, int(height*0.89)), (255, 255, 255), 25)

        cv2.imshow('frame', current)

        cv2.setMouseCallback('frame', selectZone)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    inspectAndCap('ff.mp4')
