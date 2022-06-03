# create a photo viewer with simple dialog user input for the path of the image using tkinter

# import the tkinter module
from tkinter import *
# import the filedialog module
from tkinter import filedialog
# import the messagebox module
from tkinter import messagebox
# import the PIL module
from PIL import Image, ImageTk
# import the os module
import os

# create a class for the main window
class MainWindow(Frame):
    # define the constructor
    def __init__(self, master=None):
        # call the constructor of the Frame class
        Frame.__init__(self, master)
        # create the widgets
        self.createWidgets()
        # set the title of the window
        self.master.title("Photo Viewer")
        # set the size of the window
        self.master.geometry("500x500")
        # center the window
        self.centerWindow()
        # set the background colour of the window
        self.master.configure(bg="lightgrey")
        # set the window in the middle of the screen
        self.master.update_idletasks()

    # define the function to center the window
    def centerWindow(self):
        # get the size of the screen
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        # calculate x and y coordinates to center the window
        x = int((screenWidth/2) - (500/2))
        y = int((screenHeight/2) - (500/2))
        # set the position of the window
        self.master.geometry("+{}+{}".format(x, y))

# define the function to create the widgets
    def createWidgets(self):
        # create the label
        self.label = Label(self.master, text="Enter the path of the image:", bg="lightgrey")
        # pack the label
        self.label.pack(side=TOP, fill=X)
        # create the entry
        self.entry = Entry(self.master, width=50)
        # pack the entry
        self.entry.pack(side=TOP, fill=X)
        # create the button
        self.button = Button(self.master, text="Browse", command=self.browse)
        # pack the button
        self.button.pack(side=TOP, fill=X)
        # create the label
        self.label2 = Label(self.master, text="", bg="lightgrey")
        # pack the label
        self.label2.pack(side=TOP, fill=X)
        # create the button
        self.button2 = Button(self.master, text="Show Image", command=self.showImage)
        # pack the button
        self.button2.pack(side=TOP, fill=X)
        

    # define the function to browse the file
    def browse(self):
        # get the path of the file
        path = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        # set the path of the file in the entry
        self.entry.delete(0, END)
        self.entry.insert(0, path)
        # create the label
        self.label2 = Label(self.master, text="", bg="lightgrey")
        # pack the label
        self.label2.pack(side=TOP, fill=X)

    # define the function to show the image
    def showImage(self):
        # get the path of the file
        path = self.entry.get()
        # check if the path is not empty
        if path != "":
            # check if the file exists
            if os.path.exists(path):
                # check if the file is a jpeg file
                if path.endswith(".jpg"):
                    # create the image
                    self.image = Image.open(path)
                    # convert the image to RGB
                    self.image = self.image.convert("RGB")
                    # resize the image
                    self.image = self.image.resize((500, 500), Image.ANTIALIAS)
                    # convert the image to a PhotoImage
                    self.image = ImageTk.PhotoImage(self.image)
                    # create the label
                    self.label3 = Label(self.master, image=self.image, bg="lightgrey")
                    # pack the label
                    self.label3.pack(side=TOP, fill=X)
                # if the file is not a jpeg file
                else:
                    # create the label
                    self.label2 = Label(self.master, text="The file is not a jpeg file", bg="lightgrey")
                    # pack the label
                    self.label2.pack(side=TOP, fill=X)
            # if the file does not exist
            else:
                # create the label
                self.label2 = Label(self.master, text="The file does not exist", bg="lightgrey")
                # pack the label
                self.label2.pack(side=TOP, fill=X)
        # if the path is empty
        else:
            # create the label
            self.label2 = Label(self.master, text="The path is empty", bg="lightgrey")
            # pack the label
            self.label2.pack(side=TOP, fill=X)
        # create the button
        self.button2 = Button(self.master, text="Close", command=self.closeWindow)
        # pack the button
        self.button2.pack(side=TOP, fill=X)


    # define the function to close the window
    def closeWindow(self):
        # close the window
        self.master.destroy()

        # create the main window
root = Tk()
# create the main window
app = MainWindow(root)
# set the title of the main window
root.title("Photo Viewer")
# set the size of the main window
root.geometry("500x500")
# center the main window
app.centerWindow()
# set the background colour of the main window
root.configure(bg="lightgrey")
# set the main window in the middle of the screen
root.update_idletasks()
# create the main loop
root.mainloop()
