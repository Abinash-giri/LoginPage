from tkinter import *

def main_screen():
    mainscreen = Tk()   # create a GUI window
    mainscreen.geometry("800x800") # set the configuration of GUI window
    mainscreen.title(" Login Page") # set the title of GUI window


# create a Form label
Label(text="Login Window Example", bg="blue", width="30", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()

# create Login Button
Button(text="Login", height="2", width="30").pack()
Label(text="").pack()

# create a register button
Button(text="Register", height="2", width="30").pack()

#mainscreen.mainloop()  # start the GUI
#main_screen()  # call the main_account_screen() function

if __name__ == "__main__":
    # run screen loop
    print('')
    main_screen()
    mainloop(1)
