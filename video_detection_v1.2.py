import numpy as np
import cv2
import imutils
# import thread
import time
import Queue 
# import multiprocessing as mp 
# from multiprocessing import Process
# import threading
# import thread
from multiprocessing.pool import ThreadPool

# from multiprocessing.dummy import Pool as ThreadPool

# Pool = mp.Pool()
# pool = ThreadPool(2)

cap = cv2.VideoCapture(0)
# cap.set(cv2.cv.CV_CAP_PROP_FPS, 120)

Face_cascade = cv2.CascadeClassifier('Face_Detection/haarcascade_frontalface_default.xml')
# Body_cascade = cv2.CascadeClassifier('Face_Detection/haarcascade_fullbody.xml')
# print(Face_cascade)
pool = ThreadPool(processes=5)

def Main():

    # def Classification():

    while(True):
        def Face_detection(frame):
            try:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = Face_cascade.detectMultiScale(gray, 1.2, 5)
                for (x, y, w, h) in faces: 
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

                # cropped_face = frame[x:x+h,y:y+w]
                cropped_face = frame[y:y+h, x:x+w]
                # return frame
                # q.put(cropped_face)
                q.put(frame)
                # time.sleep(timer)
            except Exception as e:
                # print e
                cropped_face = frame[20:20+40,4:4+2]
                # return cropped_face
                # return frame
                # q.put(cropped_face)
                q.put(frame)
                # time.sleep(timer)
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            try:
                q = Queue.Queue()
                frame = cv2.flip(frame, 1)

                # hello = Face_detection(frame)

                # Thread1 = threading.Thread(target=Face_detection, args=[frame, 0.0000000001])
                # Thread1.start()
                # Thread1.join()

                # thread.start_new_thread(Face_detection, (frame, 0.00000001,))
                # pool.map(Face_detection, frame)
                # pool.close()
                # pool.join()

                # t = threading.Thread(target=Face_detection, args=(frame,))
                # t.daemon = True
                # t.start()

                # p = Process(target=Face_detection, args=(frame,))
                # p.start()
                # p.join()
                task = pool.apply_async(Face_detection, (frame,))
                # task = pool.apply_async(Face_detection, (frame,))

                # task.close()    
                
                cropped = q.get()

                # frame = imutils.resize(frame, width=450)
                cv2.imshow("Frame",cropped)
                # cv2.imshow("Cropped",hello)

                if cv2.waitKey(1) == ord('q'):
                    break

            except Exception as e:
                print e 
Main()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# from multiprocessing import Process
# #omitted code
# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     # getting tick count
#     e1 = cv2.getTickCount()
#     # storing frame
#     _, img = cap.read()
#     # extract grid - first subsystem
#     # gridExtractor.extractGrid(img)
#     # define red colours in the screen - second subsystem
#     # findRedColours(img, board)
#     # getting tick count after the functions
#     e2 = cv2.getTickCount()
#     # calculating time
#     t = (e2 - e1) / cv2.getTickFrequency()
#     # print time
#     cv2.imshow("a",img)
#     print(t)

#     # check if img is none
#     if img is not None:
#         # omitted code

#         k = cv2.waitKey(20) & 0xFF
#         # start the game, hide info
#         if (k == ord('s') or k == ord('S')) and start is False:
#             # create new thread to play game
#             p = Process(target=playGame)
#             p.start()
