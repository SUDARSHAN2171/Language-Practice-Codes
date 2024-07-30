import cv2
'''
cap =cv2.VideoCapture(0);
while (True):
    ret,frame=cap.read()
    print(cap.get.(cv2.CAP_PROP_FRAME_WIDTH)) #these statements will print the heigth & width of the frame 
    print(cap.get.(cv2.CAP_PROP_FRAME_HEIGHT))
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
'''


'''
this will run the camera in grey color
cap=cv2.VideoCapture(0); #if we want to input a video instead of camera then we can write the file name instead of (0)
while(cap.isOpened):  #this will check weather the camera is correct and open or not even we can use while(True) instead of while(cap.isOpened)
    ret,frame=cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame',grey)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
'''

cap=cv2.VideoCapture(0);
fourcc =cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('Recording.avi',fourcc,20.0,(640,480))
while(cap.isOpened):
    ret,frame=cap.read()
    if ret==True:
          print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #these statements will print the heigth & width of the frame 
          print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
          out.write(frame)
          grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
          cv2.imshow('Frame',grey)
          if cv2.waitKey(1) &0xFF==ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
                