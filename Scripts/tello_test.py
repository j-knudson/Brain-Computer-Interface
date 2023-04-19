from djitellopy import Tello
import cv2, math, time

from grab_char_no_enter import grab_char_no_enter as user_input

tello = Tello()
tello.connect()

#tello.streamon()
#frame_read = tello.get_frame_read()

tello.takeoff()

while True:
    #img = frame_read.frame
    #cv2.imshow("drone", img)
    
    #key = cv2.waitKey(1) & 0xff
    #key = input("Enter a key: ")
    #print(key)
    #print(type(key))
    
    #if key == 1: # ESC
    #    break
    key = user_input()
    if key == 'w':
        print("tello.move_forward(30)")
        tello.move_forward(30)
        print("Done")
    elif key == 's':
        tello.move_back(30)
        print("tello.move_back(30)")
        print("Done")
    elif key == 'a':
        print("tello.move_left(30)")
        tello.move_left(30)
        print("Done")
    elif key == 'd':
        print("tello.move_right(30)")
        tello.move_right(30)
        print("Done")
    elif key == 'e':
        print("tello.rotate_clockwise(30)")
        tello.rotate_clockwise(30)
        print("Done")
    elif key == 'q':
        print("tello.rotate_counter_clockwise(30)")
        tello.rotate_counter_clockwise(30)
        print("Done")
    elif key == 'r':
        print("tello.move_up(30)")
        tello.move_up(30)
        print("Done")
    elif key == 'f':
        print("tello.move_down(30)")
        tello.move_down(30)
        print("Done")
    elif key == 't':
        print("tello.takeoff(30)")
        tello.takeoff()
        print("Done")
    elif key == 'l':
        print("tello.land(30)")
        tello.land()
        print("Done")