import PySimpleGUI as sg
import time

#tello imports
from djitellopy import Tello
tello = Tello()

# Define the layout for the Starting Page
layout1 = [
            [sg.Button('Brainwave Reading'), sg.Button('Transfer Data'), sg.Button('Manual Drone Control')]
          
          ]

def get_drone_action(action): ##receives action from a GUI button, executes a corresponding Tello-Drone class move action, then returns "Done"

    if action == 'backward':
        tello.move_back(30)
        print('tello.move_back(30)')           
    elif action == 'down':
        tello.move_down(30)
        print('tello.move_down(30)')
    elif action == 'forward':
        tello.move_forward(30)
        print('tello.move_forward(30)')
    elif action == 'land':
        tello.land
        print('tello.land')
    elif action == 'left':
        tello.move_left(30)
        print('tello.move_left(30)')
    elif action == 'right':
        tello.move_right(30)
        print('tello.move_right(30)')
    elif action == 'takeoff':
        tello.takeoff(30)
        print('tello.takeoff')
    elif action == 'up':
        tello.move_up(30)
        print('tello.move_up(30)')
    elif action == 'turn_left':
        tello.rotate_ccw(45)
        print('tello.rotate_ccw(45)')
    elif action == 'turn_right':
        tello.rotate_cw(45)
        print('tello.rotate_cw(45)')
    elif action == 'flip': 
        tello.flip('b')
        print("tello.flip('b')")
    
    #TODO Remove sleep
    #time.sleep(2)
    return("Done")

def brainwave_prediction_window():
    #Layout
    brainwave_prediction_layout = [[sg.Text('Brainwave')], [sg.Button('Brain', image_filename="./images/brain.png")]]

    brainwave_prediction_window = sg.Window("Brainwave Prediction", brainwave_prediction_layout, size=(1200, 800), element_justification='c')

    while True: 
        event, values = brainwave_prediction_window.read() 
        if event in (sg.WIN_CLOSED, 'Quit'):
            break
        elif event == "Brain":
            print("Big Brain ")
    
    window1.un_hide()
    brainwave_prediction_window.close() 

def manual_drone_control(items): 

    #Define the layout for the Manual Drone Control Page

    #Column layouts for centering"Done.")
    top_center = [[sg.Button('Up', size=(8,2), image_filename="./images/up.png")]]
    top_right = [[sg.Text('Flight Log')], [sg.Listbox(values=[], size=(30, 6), key='LOG')]]
    bottom_center = [[sg.Button('Down', size=(8,2), image_filename="./images/down.png")]]

    manual_drone_control_layout = [ 
                [sg.Button('Home', size=(8,2), image_filename="./images/home.png"), sg.Push(), sg.Column(top_center, pad=((55,0),(0,0))), sg.Push(), sg.Column(top_right), ],       
                [sg.Push(),sg.Push(),sg.Button('Forward', size=(8,2), image_filename="./images/forward.png"), sg.Push(), sg.Push(),], 

                [sg.Button('Turn Left', size=(8,2), image_filename="./images/turnLeft.png"),  
                sg.Button('Left', size=(8,2), image_filename="./images/left.png"),
                sg.Button(image_filename="./images/drone.png"),
                sg.Button('Right', size=(8,2), image_filename="./images/right.png"),
                sg.Button('Turn Right', size=(8,2), image_filename="./images/turnRight.png")],

                [sg.Button('Back', size=(8,2), image_filename="./images/back.png")],
                [sg.Button('Connect', size=(8,2), image_filename="./images/connect.png"), sg.Push(),sg.Push(), sg.Column(bottom_center, pad=((55,0),(0,0))), sg.Push(), sg.Button('Takeoff', size=(8,2), image_filename="./images/takeoff.png"), sg.Button('Land', size=(8,2), image_filename="./images/land.png")]]
    
    manual_drone_control_window = sg.Window('Manual Drone Control', manual_drone_control_layout, size=(1200, 800), element_justification='c')

    first_iteration = True
    
    while True:
        event, values = manual_drone_control_window.read()

        if(first_iteration):
            items.insert(0, "---------- NEW LOG ----------")
            manual_drone_control_window['LOG'].update(values=items)
            first_iteration=False

        if event == sg.WIN_CLOSED:
            manual_drone_control_window.close()
            window1.un_hide()
            break
        elif event == 'Up':
            # Code for moving the drone up
            items.insert(0, "Up button pressed")
            manual_drone_control_window['LOG'].update(values=items)
            items.insert(0, get_drone_action('up'))
            manual_drone_control_window['LOG'].update(values=items)

        elif event == 'Down':
            # Code for moving the drone down                
            items.insert(0, "Down button pressed")
            manual_drone_control_window['LOG'].update(values=items)
            items.insert(0, get_drone_action('down'))
            manual_drone_control_window['LOG'].update(values=items)
        elif event == 'Forward':
            # Code for moving the drone forward
            items.insert(0, "Forward button pressed")
            manual_drone_control_window['LOG'].update(values=items)
            items.insert(0, get_drone_action('forward'))
            manual_drone_control_window['LOG'].update(values=items)
        elif event == 'Back':
            # Code for moving the drone back                
            items.insert(0, "Back button pressed")
            manual_drone_control_window['LOG'].update(values=items)
            items.insert(0, get_drone_action('backward'))
            manual_drone_control_window['LOG'].update(values=items)
        elif event == 'Left':
            # Code for moving the drone left
            items.insert(0, "Left button pressed")
            manual_drone_control_window['LOG'].update(values=items)
            items.insert(0, get_drone_action('left'))
            manual_drone_control_window['LOG'].update(values=items)
        elif event == 'Right':
            # Code for moving the drone right
            items.insert(0, "Right button pressed")
            manual_drone_control_window['LOG'].update(values=items)
            items.insert(0, get_drone_action('right'))
            manual_drone_control_window['LOG'].update(values=items)
        elif event == 'Turn Left':
            # Code for turning the drone left
            items.insert(0, "Turn Left button pressed")
            manual_drone_control_window['LOG'].update(values=items)
            items.insert(0, get_drone_action('turn_left'))
            manual_drone_control_window['LOG'].update(values=items)
        elif event == 'Turn Right':
            # Code for turning the drone right
            items.insert(0, "Turn right button pressed")
            manual_drone_control_window['LOG'].update(values=items)
            items.insert(0, get_drone_action('turn_right'))
            manual_drone_control_window['LOG'].update(values=items)
        elif event == 'Takeoff':
            # Code for taking off the drone
            items.insert(0, "Takeoff button pressed")
            manual_drone_control_window['LOG'].update(values=items)
            items.insert(0, get_drone_action('takeoff'))
            manual_drone_control_window['LOG'].update(values=items)
        elif event == 'Land':
            # Code for landing the drone
            items.insert(0, "Land button pressed")
            manual_drone_control_window['LOG'].update(values=items)
            items.insert(0, get_drone_action('land'))
            manual_drone_control_window['LOG'].update(values=items)
        elif event == 'Home':
            # Code for Home
            items.insert(0, "home testing")
            manual_drone_control_window.close()
            window1.un_hide()
            break               
        elif event == 'Connect':
            # Code for Connect
            items.insert(0, "Connect button pressed")

            manual_drone_control_window['LOG'].update(values=items)
            tello.connect()
            time.sleep(2)
            items.insert(0, "Done.")
            manual_drone_control_window['LOG'].update(values=items)
            #TODO check on connect feedback and if more response is needed here
    

    # items.insert(0, "---------- END LOG ----------")
    window1.un_hide
    manual_drone_control_window.close()

# Define the layout for the Brainwave Reading Page
layout3 = [[sg.Button(image_filename="./images/brain.png")]]

# Define the layout for the Transfer Data Page
layout4 = [[sg.Button(image_filename="./images/upload.png")]]

# Create the windows
window1 = sg.Window('Start Page', layout1, size=(1200, 800))
window4 = sg.Window('Transfer Data', layout4, size=(1200, 800), element_justification='c')

items = []

# Event loop for the first window
while True:
    event1, values1 = window1.read()
    if event1 == sg.WIN_CLOSED:
        break
    elif event1 == 'Brainwave Reading':
        window1.hide()
        brainwave_prediction_window()
    elif event1 == 'Transfer Data':
        window1.hide()
        window4.read()
    elif event1 == 'Manual Drone Control':
        window1.hide()
        manual_drone_control(items)



