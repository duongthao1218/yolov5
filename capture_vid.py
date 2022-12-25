'''
Capture frames from video and save as JPEG images.
'''
import os
import cv2 
import sys
import argparse

def main(path_vid: str, path_imgs: str):
    cap = cv2.VideoCapture(path_vid)
    id = 0

    try:
        os.mkdir(path_imgs)
        os.mkdir(path_imgs + '/images')
    except:
        pass

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
        cv2.imwrite(path_imgs + f'/images/{id}.jpg', frame)

        id+=1


    cap.release()
    cv2.destroyAllWindows()
    sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path_vid', type=str, default='./data/videos/cars.mp4' , help='path to video')
    parser.add_argument('--path_imgs', type=str, default='./datasets/cars_1' , help='path to save images')

    opt = parser.parse_args()
    
    main(opt.path_vid, opt.path_imgs)
    