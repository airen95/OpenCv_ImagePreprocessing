import os
import cv2 as cv
import numpy as np
#list of people
p=[]
for i in os.listdir('/home/tonlee/Desktop/Practice/Open_CV/Files/Faces/train'):
    p.append(i)
print (p)
DIR=r'/home/tonlee/Desktop/Practice/Open_CV/Files/Faces/train'
haar_cascade=cv.CascadeClassifier('Detect_Face/haar_face.xml')


features=[]
labels=[]
def create_train():
    for person in p:
        path=os.path.join(DIR,person)
        label=p.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_read=cv.imread(img_path)
            gray=cv.cvtColor(img_read, cv.COLOR_BGR2GRAY)
            faces_rect=haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
            for (x,y,w,h) in faces_rect:
                face_roi=gray[y:y+h,x:x+w]
                features.append(face_roi)
                labels.append(label)
create_train()

#print('Lenght of the features %d' %len(features))
#print('Lenght of labels %d' %len(labels))
print('Training done--------------')
features=np.array(features, dtype='object')
labels=np.array(labels)
face_recognizer=cv.face.createLBPHFaceRecognizer()


#training model:
face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('label.npy',labels)