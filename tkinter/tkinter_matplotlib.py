import tkinter as tk
import math as m
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

t = []

for x in list(range(0, 101)):
    t.append(x/15.87)

def main():
    root = tk.Tk()
    gui = Window(root)
    gui.root.mainloop()
    return None

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("marriage tk and plt")
        self.root.geometry('600x500')

        self.amplitude = 1
        self.frequency = 1
        self.vertical_shift = 0
        self.phase_shift = 0


        tk.Label(self.root, text="Amplitude").grid(row=0, column=0)
        self.amplitude_entry = tk.Entry(self.root, width=5)
        self.amplitude_entry.grid(row=0, column=1)
        self.amplitude_entry.insert(0, '1.0')

        tk.Label(self.root, text="Frequency").grid(row=1, column=0)
        self.frequency_entry = tk.Entry(self.root, width=5)
        self.frequency_entry.grid(row=1, column=1)
        self.frequency_entry.insert(0, '1.0')

        tk.Label(self.root, text="Vertical Shift").grid(row=2, column=0)
        self.vertical_shift_entry = tk.Entry(self.root, width=5)
        self.vertical_shift_entry.grid(row=2, column=1)
        self.vertical_shift_entry.insert(0, '0.0')

        tk.Label(self.root, text="Phase Shift").grid(row=3, column=0)
        self.phase_shift_entry = tk.Entry(self.root, width=5)
        self.phase_shift_entry.grid(row=3, column=1)
        self.phase_shift_entry.insert(0, '0.0')

        button1 = tk.Button(self.root, text="Calculate", command=self.update_values)
        button1.grid(row=4, column=0)
        self.root.bind("<Return>", self.update_values)
        self.plot_values()
        pass

<<<<<<< HEAD
#     def update_values(self, event=None):
#         self.amplitude = float(self.amplitude_entry.get())
#         self.phase_shift = float(self.phase_shift_entry.get())
#         self.vertical_shift = float(self.vertical_shift_entry.get())
#         self.frequency = float(self.frequency_entry.get())
#         self.plot_values()
#         return None
=======
    def update_values(self, event=None):
        self.amplitude = float(self.amplitude_entry.get())
        self.phase_shift = float(self.phase_shift_entry.get())
        self.vertical_shift = float(self.vertical_shift_entry.get())
        self.frequency = float(self.frequency_entry.get())
        self.plot_values()
        
        # return None
>>>>>>> dc3779291a520ca16ca7e85adb72452b5589c19a

    def plot_values(self):
        y = []
        for x in t:
            y.append(self.amplitude * m.sin(self.frequency * x + self.phase_shift)\
                    + self.vertical_shift)

        figure = plt.figure(figsize = (5,4), dpi=100)
        figure.add_subplot(111).plot(t,y)
        chart = FigureCanvasTkAgg(figure, self.root)
        chart.get_tk_widget().grid(row=5, column=0)

        plt.grid()
        plt.title("Sinus-Function")
        plt.xlim(0, 6.3)
        plt.ylim(-3, 3)

    pass

main()
