#coding=utf-8
import cv2
import face_recognition
import os

class face():
    def __init__(self):
        self.path = "sanye" 
        self.total_image_name = []
        self.total_face_encoding = []
        self.loadface(self.path)

    def loadface(self, path):
        for fn in os.listdir(path):
            self.total_face_encoding.append(
                face_recognition.face_encodings(
                    face_recognition.load_image_file(path + "/" + fn))[0])
            fn = fn[:(len(fn) - 4)]  
            self.total_image_name.append(fn) 

    def faceai(self, filename):
        frame = cv2.imread(filename)
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        isshe = False
        for (top, right, bottom, left), face_encoding in zip(
                face_locations, face_encodings):
            for i, v in enumerate(self.total_face_encoding):
                match = face_recognition.compare_faces(
                    [v], face_encoding, tolerance=0.5)
                if match[0]:
                    isshe = True
                    break
        return isshe

    def cutPhone(self, model_name,images_path):
        filesname = os.listdir(images_path)
        for filed in filesname:
            filepath = images_path + "/" + filed
            frame = cv2.imread(filepath)
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)
            for (top, right, bottom, left), face_encoding in zip(
                    face_locations, face_encodings):
                testImg = frame[top:bottom,left:right]
                cv2.imwrite('sanye/sanye_%s.jpg' % model_name, testImg,[int(cv2.IMWRITE_PNG_COMPRESSION), 0])