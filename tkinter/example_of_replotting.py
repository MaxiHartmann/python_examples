import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = tk.Tk()
root.geometry('600x500+10+10')

def do_plot(x, y, idx):
    [ax[x].clear() for x in range(4)]
    ax[idx].plot(x,y)
    canvas.draw()

def plot_sin():
    idx=3
    ax[idx].clear()
    xmin=0
    xmax=10
    amp=2
    x=np.linspace(xmin, xmax, 20)
    y=amp*np.sin(x)
    ax[idx].plot(x, y)
    ax[idx].set_xlim(xmin, xmax)
    ax[idx].set_ylim(-amp*1.1, amp*1.1)
    canvas.draw()

def plot_cos():
    idx=3
    ax[idx].clear()
    x=np.linspace(0, 7, 20)
    y=np.cos(x)
    ax[idx].plot(x, y)
    ax[idx].set_xlim(0, 10)
    ax[idx].set_ylim(0, 1)
    canvas.draw()

frame1 = tk.Frame(root)
frame1.place(x=0, y=0, width=500, height=500)

figure = plt.Figure(figsize=(5,5), facecolor='grey')
canvas = FigureCanvasTkAgg(figure, frame1)
canvas.get_tk_widget().place(x=0, y=0, width=500, height=500)

# ax = [figure.add_subplot(2, 2, x+1) for x in range(4)]
ax1 = figure.add_subplot(2, 2, 1)
ax2 = figure.add_subplot(2, 2, 2)
ax3 = figure.add_subplot(2, 2, 3)
ax4 = figure.add_subplot(2, 2, 4)
ax=[ax1, ax2, ax3, ax4]

frame2 = tk.Frame(root); 
frame2.place(x=500, y=0, width=100, height=400)

btplot1 = tk.Button(frame2, text='plot 1', command= lambda: do_plot([0,1,2],[5,3,7], 1))
btplot1.place(x=0, y=50, width=50, height=20)

btplot2 = tk.Button(frame2, text='plot 2', command= lambda: do_plot([5,6,7],[3,8,2], 2))
btplot2.place(x=0, y=100, width=50, height=20)

btplot3 = tk.Button(frame2, text='sin(x)', command=plot_sin)
btplot3.place(x=0, y=150, width=50, height=20)

btplot4 = tk.Button(frame2, text='cos(x)', command=plot_cos)
btplot4.place(x=0, y=200, width=50, height=20)

root.mainloop()
