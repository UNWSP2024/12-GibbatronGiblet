import tkinter
import tkinter.messagebox

class RepairJob:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title('Repair Job Details')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.oil_var = tkinter.IntVar()
        self.lube_var = tkinter.IntVar()
        self.radiator_var = tkinter.IntVar()
        self.transmission_var = tkinter.IntVar()
        self.inspection_var = tkinter.IntVar()
        self.muffler_var = tkinter.IntVar()
        self.tire_rotation_var = tkinter.IntVar()

        self.oil_var.set(0)
        self.lube_var.set(0)
        self.radiator_var.set(0)
        self.transmission_var.set(0)
        self.inspection_var.set(0)
        self.muffler_var.set(0)
        self.tire_rotation_var.set(0)

        self.oil_change = tkinter.Checkbutton(self.top_frame,
                        text="Oil Change", variable = self.oil_var, command = self.reciept)

        self.lube_job = tkinter.Checkbutton(self.top_frame,
                        text="Lube Job", variable = self.lube_var, command = self.reciept)

        self.radiator_flush = tkinter.Checkbutton(self.top_frame,
                        text = "Radiator Flush", variable = self.radiator_var, command = self.reciept)

        self.transmission_fluid = tkinter.Checkbutton(self.top_frame,
                        text = "Transmission Fluid", variable = self.transmission_var, command = self.reciept)

        self.inspection = tkinter.Checkbutton(self.top_frame,
                        text = "Inspection", variable = self.inspection_var, command = self.reciept)

        self.muffler_replacement = tkinter.Checkbutton(self.top_frame,
                        text = "Muffler Replacement", variable = self.muffler_var, command = self.reciept)

        self.tire_rotation = tkinter.Checkbutton(self.top_frame,
                        text = "Tire Rotation", variable = self.oil_var, command = self.reciept)

        self.total_var = tkinter.StringVar()

        self.total_label = tkinter.Label(self.bottom_frame,
                                         textvariable = self.total_var)



        self.top_frame.pack()
        self.bottom_frame.pack()
        self.oil_change.pack(side='left')
        self.lube_job.pack(side='left')
        self.radiator_flush.pack(side='left')
        self.transmission_fluid.pack(side='left')
        self.inspection.pack(side='left')
        self.muffler_replacement.pack(side='left')
        self.total_label.pack(side='left')

        tkinter.mainloop()

    def reciept(self):
            total = 0
        # while True:
            if self.oil_var.get() == 1:
                total = 30
                self.total_var.set(f'Your repair will cost ${total:.2f}')
            if self.lube_var.get() == 1:
                total += 20
                self.total_var.set(f'Your repair will cost ${total:.2f}')
            if self.radiator_var.get() == 1:
                total += 40
                self.total_var.set(f'Your repair will cost ${total:.2f}')
            if self.transmission_var.get() == 1:
                total += 100
                self.total_var.set(f'Your repair will cost ${total:.2f}')
            if self.inspection_var.get() == 1:
                total += 35
                self.total_var.set(f'Your repair will cost ${total:.2f}')
            if self.muffler_var.get() == 1:
                total += 200
                self.total_var.set(f'Your repair will cost ${total:.2f}')
            if self.tire_rotation_var.get() == 1:
                total += 20
                self.total_var.set(f'Your repair will cost ${total:.2f}')
            else:
                self.total_var.set(f'Your repair will cost ${total:.2f}')


my_repair_job = RepairJob()
#This program was written on 11/22/25 by Logan Gibson
#Its name is "Joe's Automotive"