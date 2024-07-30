import cv2
#there are various modes to read a image 
#-1 - This will open image as it is with alpha channels
#0 - this will open image in white and black 
#1 -  this will just open the image as it is
img=cv2.imread("ExampleForRWS.jpg",1)
print(img)#this will print the image in the form of pixels

#show image
cv2.imshow('ExampleForRWS.jpg',img) #using this imshow the image will be visible for few millesecond but not properly visiable

#waiting key 
k=cv2.waitKey(0)#waitKey is used to make the popping image screen wait for specific duration if (0) is passed then the screen will remain on till we dont close

#Destroy all windows
if k==27: #this is the ASCII Value for escape button
    cv2.destroyAllWindows()
elif k==ord('S'): #ord is a built in function to take keyboard values in this case it's S
#write a image
    cv2.imwrite('CopyImage.png',img)#this will create a copy image of the original
    cv2.destroyAllWindows() 
    