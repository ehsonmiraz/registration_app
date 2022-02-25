import sys
import os

import pickle
import urllib
import pyrebase
from services.genrate_encodings import generateEncodings


class CloudService:
#setting up firebase
    firebaseConfig={}
    id=0

    def __init__(self,):
     
      firebaseConfig = {
      "apiKey" : "AIzaSyCea6QfQMpO8m2kRDbk-1asxorhU48gvzU",
      "authDomain" : "attendenceapp-9f2d0.firebaseapp.com",
      "projectId" : "attendenceapp-9f2d0",
      "storageBucket" : "attendenceapp-9f2d0.appspot.com",
      "messagingSenderId" : "155033444662",
      "appId" : "1:155033444662:web:80275f14ec309bfdf89397",
      "measurementId" : "G-TBGSY819YL",
      "databaseURL" : "",
      "serviceAccount": "services\servicekey.json"
       };

      firebase=pyrebase.initialize_app(firebaseConfig)
    #define storage
      self.storage=firebase.storage()
    def pickl(self,encodings):
        file=open("temp.pkl", "wb")
        pickle.dump(encodings, file)
        file.close()
    def unppickl(self,):
        pass

    def download(self):
      offlineEncoList=list(map(lambda i : "face_encodings/"+ i, os.listdir("../face_encodings/")))
      onlineEncoList=list(map(lambda file_obj : file_obj.name,self.storage.child("face_encodings/").list_files()))
      onlineEncoList=list(filter(lambda  file_name : "face_encodings/" in file_name ,onlineEncoList))


     # print(len(onlineEncoList))
      for file in onlineEncoList:
          if file in offlineEncoList:
              continue
          try:
              print(file)
              online_path=file
              url=self.storage.child(online_path).get_url(None)
              self.storage.child(online_path).download(file,file.split('/')[1])
          except Exception as e:
              print(e)
              print('Download Failed')




    def uploader(self):
        cloudfilename="face_encodings/"+str(self.id)+'.pkl'
        self.storage.child(cloudfilename).put("temp.pkl")

    def inputID(self):
        id=input("enter your id : ")
        return id
    def addFace(self):
        encoding=generateEncodings()
        self.id=self.inputID()
        if(len(encoding)is not 10 or id<0):
            print("error .../")
            return
        #pickle into temp and upload a file
        self.pickl(encoding)
        self.uploader()


if __name__=="__main__":
    Driver = CloudService()
    Driver.uploader()
