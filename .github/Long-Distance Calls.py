import tkinter
import tkinter.messagebox

class DistantCall:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Distance Calls')

        # self.main_window.title('Long Distance Calls')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.button_var = tkinter.IntVar()
        self.button_var.set(0)

        self.day_time_button = tkinter.Radiobutton(self.top_frame,
                            text = 'Daytime (6:00 A.M. through 5:59 P.M.)',
                           variable = self.button_var, value = 1)

        self.evening_button = tkinter.Radiobutton(self.top_frame,
                            text = 'Evening (6:00 P.M.  through 11:59 P.M.)',
                            variable = self.button_var, value = 2)
        self.off_peak_button = tkinter.Radiobutton(self.top_frame,
                                text = "Off-Peak (midnight through 5:59 P.M)",
                                variable = self.button_var, value = 3)
        self.prompt_label = tkinter.Label(self.bottom_frame, text = 'Enter the minutes spent calling:')
        self.enter_minutes = tkinter.Entry(self.bottom_frame, width = 10)

        self.calc_button = tkinter.Button(self.bottom_frame,
                            text = 'Calculate Cost', command = self.calc_cost)

        self.top_frame.pack()
        self.bottom_frame.pack()
        self.day_time_button.pack()
        self.evening_button.pack()
        self.off_peak_button.pack()
        self.prompt_label.pack()
        self.enter_minutes.pack()
        self.calc_button.pack()

        tkinter.mainloop()

    def calc_cost(self):
        call_time = float(self.enter_minutes.get())
        if self.button_var.get() == 1:
            call_cost = .02
            tkinter.messagebox.showinfo("Cost Info", f'Your call costed ${call_cost * call_time:.2f}.')
        elif self.button_var.get() == 2:
            call_cost = .12
            tkinter.messagebox.showinfo("Cost Info", f'Your call costed ${call_cost * call_time:.2f}.')
        elif self.button_var.get() == 3:
            call_cost = .05
            tkinter.messagebox.showinfo("Cost Info", f'Your call costed ${call_cost * call_time:.2f}.')
        else:
            tkinter.messagebox.showinfo("Cost Info", "Invalid input.")

my_call = DistantCall()


#This program was written on 11/23/25 by Logan Gibson
#Its name is "Long-Distance Calls"