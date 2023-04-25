import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master
        master.title('Main Screen')

        # create three buttons on the main screen
        self.btn1 = tk.Button(master, text='Screen 1',
                              command=self.open_screen1)
        self.btn1.pack(pady=10)

        self.btn2 = tk.Button(master, text='Screen 2',
                              command=self.open_screen2)
        self.btn2.pack(pady=10)

        self.btn3 = tk.Button(master, text='Screen 3',
                              command=self.open_screen3)
        self.btn3.pack(pady=10)

    def open_screen1(self):
        # create a new screen with a button and a textbox
        self.screen1 = tk.Toplevel(self.master)
        self.screen1.title('Screen 1')

        self.input1 = tk.Entry(self.screen1)
        self.input1.pack(pady=10)

        self.submit1 = tk.Button(
            self.screen1, text='Submit', command=self.submit_screen1)
        self.submit1.pack(pady=10)

    def submit_screen1(self):
        # retrieve the input text from the textbox and print it to the console
        input_text = self.input1.get()
        print(f'Screen 1: Input Text: {input_text}')

    def open_screen2(self):
        # create a new screen with a button and a textbox
        self.screen2 = tk.Toplevel(self.master)
        self.screen2.title('Screen 2')

        self.input2 = tk.Entry(self.screen2)
        self.input2.pack(pady=10)

        self.submit2 = tk.Button(
            self.screen2, text='Submit', command=self.submit_screen2)
        self.submit2.pack(pady=10)

    def submit_screen2(self):
        # retrieve the input text from the textbox and print it to the console
        input_text = self.input2.get()
        print(f'Screen 2: Input Text: {input_text}')

    def open_screen3(self):
        # create a new screen with a button and a textbox
        self.screen3 = tk.Toplevel(self.master)
        self.screen3.title('Screen 3')

        self.input3 = tk.Entry(self.screen3)
        self.input3.pack(pady=10)

        self.submit3 = tk.Button(
            self.screen3, text='Submit', command=self.submit_screen3)
        self.submit3.pack(pady=10)

    def submit_screen3(self):
        # retrieve the input text from the textbox and print it to the console
        input_text = self.input3.get()
        print(f'Screen 3: Input Text: {input_text}')


root = tk.Tk()
app = App(root)
root.mainloop()


# make a gui interface here

# main menu:
# option 1 -- manual controls
# -- connect to drone wifi --
# use WASD to manipulate Drone
# use Q to quit program


# option 2 -- BCI Control
# -- connect to drone wifi --
# -- turn on and wear the bci headset --
# -- ensure cyton dongle is connected to your computer and BCI app is open --
# push button to send command --> brainflow session is activated and eeg brainwave data is gathered --> data is send to the server via /predictthought --> prediction as a response
# use prediction response to command the drone
# once drone finished action prompt user to send another thought


# option 3 -- live prediction transfer
