'''
The goal is to creat a script that read a video file
Play it and allow users to capture and save certain frames

Current progress: |##########          | 50% filling details
'''


def inspectAndCap(fileName, grayScale = False, maxRes = 960):
    import cv2
    import numpy as np

    cap = cv2.VideoCapture(fileName)
    index = 0
    showInstructions = False
    ret, sample = cap.read()
    height, width, channels = sample.shape
    rectLoc_1 = (height//16 ,width//20)
    rectLoc_2 = (width//3, height//8)
    textLoc = (height//15 ,width//15)
    instructions = ['Right Arrow Key: Next Frame',
                    'Left Arrow Key: Last Frame',
                    'S: Start Recording Frames',
                    'R: Record Current Frame',
                    'Q: Quit']
    while(True):

        cap.set(1, index)
        ret, frame = cap.read()
        current = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) if grayScale else frame


        cv2.rectangle(current, rectLoc_1, rectLoc_2, (0,0,0) ,50)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(current,'frame {}, total second {}'.format(index, index//24),
                    textLoc, font, 1, (255,255,255), 2, cv2.LINE_AA)
        

        

        #Left: 2424832 Up: 2490368 Right: 2555904 Down: 2621440
        key = cv2.waitKeyEx(0)
        if key == 2555904: index += 1
        elif key == 2424832: index -= 1
        elif key == ord('q'): break
        elif key == ord('i'): showInstructions = ~showInstructions

        if showInstructions:
            for i, text in zip(np.arange(1, 6, 1), instructions):
                cv2.putText(current, text, 
                        (height//15, width//15 + i*width//30), font, 1, (255,255,255), 2, cv2.LINE_AA)

        cv2.imshow('frame', current)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    inspectAndCap('ff.mp4')
