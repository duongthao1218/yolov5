'''
Capture frames from video and save as JPEG images.
'''
import cv2 
import sys
import argparse

def main(path: str):
    cap = cv2.VideoCapture(path)
    id = 0

    while True:
        ret, frame = cap.read() 

        if not ret:
            print('Cant capture video')
            break

        # Show frame on window
        cv2.imshow('Display',frame)

        k = cv2.waitKey(1)

        # Press 'q' on the keyboard to quit program
        if k == ord('q'):
            break

        # Save the frame as JPEG file
        cv2.imwrite(f'./data/images/{id}.jpg', frame)

        id+=1


    cap.release()
    cv2.destroyAllWindows()
    sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='./data/videos/cars.mp4' , help='path to video')
    opt = parser.parse_args()
    
    main(opt.path)
    