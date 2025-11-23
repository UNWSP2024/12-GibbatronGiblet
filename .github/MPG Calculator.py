import tkinter
import tkinter.messagebox

class MilesPerGallon:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Miles Per Gallon Calculator")
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.miles_label = tkinter.Label(self.top_frame,
                        text="Enter The Miles Your Car Can Travel: ")
        self.gallons_label = tkinter.Label(self.bottom_frame,
                        text="Enter The Tank's Capacity In Gallons: ")
        self.miles_entry = tkinter.Entry(self.top_frame)

        self.gallons_entry = tkinter.Entry(self.bottom_frame)

        self.value = tkinter.StringVar()
        self.MPG_label = tkinter.Label(self.bottom_frame,
                    textvariable=self.value)
        self.calculate_button = tkinter.Button(self.bottom_frame,text='Calculate',
                                               command=self.convert)


        self.top_frame.pack()
        self.bottom_frame.pack()
        self.miles_label.pack()
        self.gallons_label.pack()
        self.miles_entry.pack()
        self.gallons_entry.pack()
        self.MPG_label.pack()
        self.calculate_button.pack()

        tkinter.mainloop()

    def convert(self):
        miles = float(self.miles_entry.get())
        gallons = float(self.gallons_entry.get())
        MPG = f'{miles/gallons:.2f}'
        self.value.set(f'Your car gets {MPG} miles per gallon.')

my_gui = MilesPerGallon()

#This program was written on 11/22/25 by Logan Gibson
#Its name is "Miles Per Gallon Calculator"

