from django.shortcuts import render
import cv2

def button(request):
    return render(request, "home.html")

def output(request):

    face_detector=cv2.CascadeClassifier('D:\\Python\\AI\\DjangoTRY\\buttons\\buttons\\haarcascade_frontalface_default.xml')
    smile_detector=cv2.CascadeClassifier('D:\\Python\\AI\\DjangoTRY\\buttons\\buttons\\haarcascade_smile.xml')

    webcam=cv2.VideoCapture(0)

    while True:

            successful_frame, frame= webcam.read()

            if not successful_frame:
                break

            grey_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

            faces=face_detector.detectMultiScale(grey_frame)
        

            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)


                the_face=frame[y:y+h , x:x+w]

                grey_face=cv2.cvtColor(the_face,cv2.COLOR_BGR2GRAY)

                smiles=smile_detector.detectMultiScale(grey_face,
                scaleFactor=1.7, minNeighbors=20)

                #Just un comment this code if you want to see a rectangle around your Smiles
                # for (x_,y_,w_,h_) in smiles:
                #     cv2.rectangle(the_face,(x_,y_),(x_+w_,y_+h_),(50,200,20),2)


                if len(smiles)>0:
                    
                    cv2.putText(frame, 'smiling', (x,y+h+40),fontScale=1.5,
                    fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255,255,255))
            cv2.imshow('Smile Detection', frame)
            key=cv2.waitKey(1)
                

            if key==81 or key==113:
                break 


    webcam.release()
    cv2.destroyAllWindows()
    print('Code Completed')
    return render(request,"home.html")

