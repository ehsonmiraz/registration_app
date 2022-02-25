#genrates encodings of len 10 via webcam

import os
from typing import List

from numpy import ndarray


def generateEncodings():
          import cv2
          import face_recognition
          import time

          FRAME_THICKNESS = 3
          FONT_THICKNESS = 2
          MODEL = "hog" #cnn
          counter=1
          encodingList=[]
          print("starting capturing...../")
         # time.sleep(2)
          cap  = cv2.VideoCapture(0)
          while True:
               success, image = cap.read()
               if( not success):
                   print("unable to read")
                   continue
               print(success)
               #if(image)
               image=cv2.resize(image,(480,360) )

               locations = face_recognition.face_locations(image, model = MODEL)
               encodings = face_recognition.face_encodings(image,locations)
             #image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
               if(len(locations) is 0 ):
                  cv2.imshow("frame",image)
                  print("faces not enough")
                  time.sleep(2)
                  key=cv2.waitKey(10)
                  if(key==ord('q') or counter>10):
                    break
                  continue
               face_location=locations[0]
               encoding=encodings[0]
               top_left = (face_location[3],face_location[0])
               bottom_right = (face_location[1],face_location[2])
               color = [ 0,0,255]
               cv2.rectangle(image,top_left,bottom_right,color,FRAME_THICKNESS)
               cv2.imshow("frame",image)
               encodingList.append(encoding)
               print("Photo "+str(counter) +" clicked")
               counter+=1
               time.sleep(2)
               key=cv2.waitKey(1)
               if(key==ord('q') or counter>10):
                  break


          cv2.destroyAllWindows()
          cap.release()
          return encodingList

if __name__=='__main__' :
  print(len(generateEncodings()))
