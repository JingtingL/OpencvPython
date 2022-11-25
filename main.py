import cv2
import numpy as np
#Defining basic functions that we use most often in open cv projects

#gray scaling the image
img = cv2.imread("485B4CE1-6AF0-4361-BBC7-A0D9167F9B5B_1_102_o.jpeg")
kernel = np.ones((5,5),np.uint8)
#convert image to gray scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#convert image to blur
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
#Find the edges
imgCanny = cv2.Canny(img,200,300)

imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
#eroding an image
imgEroded = cv2.erode(imgDilation,kernel, iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDilation)
cv2.imshow("Eroded Image",imgEroded)

cv2.waitKey(0)


'''
cap = cv2.VideoCapture(0)
#changing width
cap.set(3,640)
#changing height
cap.set(4,480)
#changing brightness
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

'''
cap = cv2.VideoCapture("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

'''
#getting an image and storing it in the img variable
img = cv2.imread("485B4CE1-6AF0-4361-BBC7-A0D9167F9B5B_1_102_o.jpeg")
#resizing the image
dsize = (100,100)
#cv2.resize(image_to_resize,the tuple size, idk what this is)
img = cv2.resize(img, dsize, interpolation=cv2.INTER_CUBIC)
#telling the computer to output the image
cv2.imshow("Outshow", img)
#this is the infinite waittime
cv2.waitKey(0)
'''

'''
print("Package Imported")
'''


# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
