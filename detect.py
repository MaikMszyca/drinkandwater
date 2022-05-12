import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0

def get_images():
    
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        
    return ret, frame

cam.release()

cv2.destroyAllWindows()

if __name__=='__main__':

    while(True):
        ret, frame = get_images()



