import tkinter
from tkinter import *
from tkinter import ttk
from pylab import *
# Importing all the required Libraries
def delete1():
  screentrigo.destroy()

def delete2():
  screenstraight.destroy()
def delete3():
  screenparabola.destroy()
def delete4():
  screenellipse.destroy()
def delete5():
  screenhyperbola.destroy()
  
##from matplotlib.backends.backend_tkagg import (
##    FigureCanvasTkAgg, NavigationToolbar2Tk)

#Importing matplotlib
import matplotlib.pyplot as mpl

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

#Impoting numpy

import numpy as np

#Defining values for x and y
x = np.linspace(-50, 51, 200)
y = np.linspace(-50, 51, 200)
#meshgrid makes an array, this is useful in defining functions
x, y = np.meshgrid(x, y)

#Axes() as a function, this will highlight our origin
def axes():
    mpl.grid()
    mpl.axhline(0, alpha= .2, linewidth= 2, color='k' )
    #Printing Horizontal line, X axis
    mpl.axvline(0, alpha= .2, linewidth= 2, color='k' )
    #Printing Vertical line, Y axis
    #mpl.axis('equal')


def Trigo():
    global screentrigo
    print('Trigo working')
    # rendering area
    figure(figsize=(8,5), dpi=80)

    # display area to use; can be modified to accomodate more graphs
    subplot(111)

    # range
    x = np.linspace((-2 * np.pi), (2 * np.pi), 256,endpoint=True)
    def sin():
        plot(x, sine, color="red", linewidth=2.5, linestyle="-", label="sin")
        ax = gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data',0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data',0))

        # x tick limits and labels
        xlim(x.min()*1.1, x.max()*1.1)
        xticks([(-2 * np.pi), (-3 * np.pi/2), -np.pi, -np.pi/2, 0, np.pi/2, np.pi, (3 * np.pi/2), (2 * np.pi)], [r'$-2\pi$', r'$-3/2\pi$', r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$', r'$3/2\pi$', r'$2\pi$'])

        # y tick limits and labels
        ylim(-4, 4)
        yticks([-4, -3, -2, -1, +1, +2, +3, +4], [r'$-4$', r'$-3$', r'$-2$', r'$-1$', r'$+1$', r'$+2$', r'$+3$', r'$+4$'])

        # legend
        legend(loc='upper left')

        for label in ax.get_xticklabels() + ax.get_yticklabels():
          label.set_fontsize(16)
          label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))

        # display
        show()
    def cos():
        x = np.linspace(-3*np.pi,3*np.pi,100)
        axes()
        y = np.cos(x)
        for i in (-3*np.pi,3*np.pi,np.pi/2):
            mpl.plot(i,0,'.')
        mpl.axhline(1, alpha= .2, linewidth= 2, color='g' )
        mpl.axhline(-1, alpha= .2, linewidth= 2, color='g' )
        
        mpl.xlabel('Angle-Input')
        mpl.ylabel('Integer-Output')
        mpl.axis('equal')
        mpl.grid()
        mpl.plot(x,y)
        mpl.show()

    '''def tan():
        ##x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
plt.plot(x, np.tan(x))
plt.ylim(-5, 5)
        ##x = np.linspace(-3*np.pi,3*np.pi,100)

        axes()
        y = np.tan(x)
        for i in (-3*np.pi,3*np.pi,np.pi/2):
            mpl.plot(i,0,'.')
        mpl.axhline(1, alpha= .2, linewidth= 2, color='g' )
        mpl.axhline(-1, alpha= .2, linewidth= 2, color='g' )
        
        mpl.xlabel('Angle-Input')
        mpl.ylabel('Integer-Output')
        mpl.axis('equal')
        mpl.grid()
        mpl.plot(x,y)
        mpl.show()'''

    def cot():
        x = np.linspace(-3*np.pi,3*np.pi,100)
        axes()
        y = 1/np.tan(x)
        for i in (-3*np.pi,3*np.pi,np.pi/2):
            mpl.plot(i,0,'.')
        mpl.axhline(1, alpha= .2, linewidth= 2, color='g' )
        mpl.axhline(-1, alpha= .2, linewidth= 2, color='g' )
        
        mpl.xlabel('Angle-Input')
        mpl.ylabel('Integer-Output')
        mpl.axis('equal')
        mpl.grid()
        mpl.plot(x,y)
        mpl.show()

    def sec():
        x = np.linspace(-3*np.pi,3*np.pi,100)
        axes()
        y = 1/np.cos(x)
        for i in (-3*np.pi,3*np.pi,np.pi/2):
            mpl.plot(i,0,'.')
        mpl.axhline(1, alpha= .2, linewidth= 2, color='g' )
        mpl.axhline(-1, alpha= .2, linewidth= 2, color='g' )
        
        mpl.xlabel('Angle-Input')
        mpl.ylabel('Integer-Output')
        mpl.axis('equal')
        mpl.grid()
        mpl.plot(x,y)
        mpl.show()

    def cosec():
        x = np.linspace(-3*np.pi,3*np.pi,100)
        axes()
        y = 1/np.sin(x)
        for i in (-3*np.pi,3*np.pi,np.pi/2):
            mpl.plot(i,0,'.')
        mpl.axhline(1, alpha= .2, linewidth= 2, color='g' )
        mpl.axhline(-1, alpha= .2, linewidth= 2, color='g' )
        
        mpl.xlabel('Angle-Input')
        mpl.ylabel('Integer-Output')
        mpl.axis('equal')
        mpl.grid()
        mpl.plot(x,y)
        mpl.show()

    def sin2x():
        x = np.linspace(-3*np.pi,3*np.pi,100)
        axes()
        y = np.sin(2*x)
        for i in (-3*np.pi,3*np.pi,np.pi/2):
            mpl.plot(i,0,'.')
        mpl.axhline(1, alpha= .2, linewidth= 2, color='g' )
        mpl.axhline(-1, alpha= .2, linewidth= 2, color='g' )
        
        mpl.xlabel('Angle-Input')
        mpl.ylabel('Integer-Output')
        mpl.axis('equal')
        mpl.grid()
        mpl.plot(x,y)
        mpl.show()

    def cos2x():
        x = np.linspace(-3*np.pi,3*np.pi,100)
        axes()
        y = np.cos(2*x)
        for i in (-3*np.pi,3*np.pi,np.pi/2):
            mpl.plot(i,0,'.')
        mpl.axhline(1, alpha= .2, linewidth= 2, color='g' )
        mpl.axhline(-1, alpha= .2, linewidth= 2, color='g' )
        
        mpl.xlabel('Angle-Input')
        mpl.ylabel('Integer-Output')
        mpl.axis('equal')
        mpl.grid()
        mpl.plot(x,y)
        mpl.show()

    def tan2x():
        x = np.linspace(-3*np.pi,3*np.pi,100)
        axes()
        y = np.tan(2*x)
        for i in (-3*np.pi,3*np.pi,np.pi/2):
            mpl.plot(i,0,'.')
        mpl.axhline(1, alpha= .2, linewidth= 2, color='g' )
        mpl.axhline(-1, alpha= .2, linewidth= 2, color='g' )
        
        mpl.xlabel('Angle-Input')
        mpl.ylabel('Integer-Output')
        mpl.axis('equal')
        mpl.grid()
        mpl.plot(x,y)
        mpl.show()






    screentrigo = Toplevel(screenloop)
    screentrigo.title('TrigoFunctions')
    screentrigo.geometry("1080x720")
    Label(screentrigo, text = "Graphs with Matpltlib -- TrigoFunctions", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='sine',height = "2", width = "30", command = sin ).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='Cos',height = "2", width = "30",).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='Tan',height = "2", width = "30",).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='Cot',height = "2", width = "30",).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='cosec',height = "2", width = "30", ).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='sec',height = "2", width = "30",).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='sin2x',height = "2", width = "30",).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='Cox2x',height = "2", width = "30", ).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='Tan2x',height = "2", width = "30", ).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='Back to Homescreen',height = "2", width = "30",command= delete1 ).pack()
    
    
def paraclick():
    if paracombo.get() == "PARABOLA STANDARD EQUATION" :
        a = IntVar ()
        Label(screenparabola, text ="Please enter the value of A").pack()
        Entry(screenparabola, textvariable = a)
        Button(screenparabola, command = parastd )
        def parastd():
            parabola = (y**2 - 4*a*x)
            #Defining values for x and y
            x = np.linspace(-50, 51, 200)
            y = np.linspace(-50, 51, 200)
            #meshgrid makes an array, this is useful in defining functions
            x, y = np.meshgrid(x, y)
            mpl.axvline(-a)
            mpl.contour(x, y, parabola, [0], colors='r' )
            mpl.show()
    elif paracombo.get() == "PARABOLA EXPANDED EQUATION" :
        a = IntVar ()
        Label(screenparabola, text ="Please enter the value of A").pack()
        Entry(screenparabola, textvariable = a)
        
        b = IntVar ()
        Label(screenparabola, text ="Please enter the value of A").pack()
        Entry(screenparabola, textvariable = b)
        
        c = IntVar ()
        Label(screenparabola, text ="Please enter the value of A").pack()
        Entry(screenparabola, textvariable = c)
        
        f = IntVar ()
        Label(screenparabola, text ="Please enter the value of A").pack()
        Entry(screenparabola, textvariable = a)
        
        g= IntVar ()
        Label(screenparabola, text ="Please enter the value of A").pack()
        Entry(screenparabola, textvariable = a)

        h = IntVar ()
        Label(screenparabola, text ="Please enter the value of A").pack()
        Entry(screenparabola, textvariable = h)
        Button(screenparabola, command = paraexpd )

        def paraexpd ():
            axes()
            mpl.contour(x, y,(a*x**2 + h*x*y + b*y**2 + g*x + f*y + c), [0], colors='k')
            mpl.show()





paradrop = ["(Select)","PARABOLA STANDARD EQUATION", "PARABOLA EXPANDED EQUATION"]

def CalulateST():
    print('straightlineX')
    print('1. Parabola in standard equation')
    a = float(straightlineX)
    parabola = (y**2 - 4*a*x)
    axes()
    mpl.contour(x, y, parabola, [0], colors='k')
    mpl.show()
    

def StraightBut():
  global screenstraight
  print('StraightBut Working')
  screenstraight = Toplevel(screenloop)
  screenstraight.title("Straightlines")
  screenstraight.geometry("1080x720")
  Label(screenstraight, text = "Graphs with Matpltlib -- Straightlines", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  global straightlineX
  global straightlineY
  global straightlineK
  
  straightlineX = IntVar()
  straightlineY = IntVar()

  Label(screenstraight, text = "Please enter details below").pack()
  Label(screenstraight, text = "", bg = "#A55D35").pack()
  Label(screenstraight, text = "Coefficient of X").pack()
 
  straightlineX_entry = Entry(screenstraight, textvariable = straightlineX)
  straightlineX_entry.pack()
  Label(screenstraight, text = "").pack()
  Label(screenstraight, text = "Coefficient of Y").pack()
  straightlineY_entry =  Entry(screenstraight, textvariable = StraightlineY)
  straightlineY_entry.pack()

  Button(screenstraight, text = "Calculate", width = 10, height = 1, command = CalulateST).pack()
  Button(screenstraight, text = "back to homescreen", width = 10, height = 1, command = delete2).pack()
def ParabolaBut():
  global screenparabola
  screenparabola = Toplevel(screenloop)
  screenparabola.title("Parabola")
  screenparabola.geometry("720x720")
  Label(screenparabola, text = "Graphs with Matpltlib -- Parabola ", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()  
  print('BEFORE')
  paracombo = ttk.Combobox(screenparabola,height = "2", width = "30",value = paradrop)
  paracombo.current(0)
  paracombo.bind('<<ComboBoxSelected>>', paraclick)
  paracombo.pack()  
  print('AFTER')
  Button(screenparabola, text = "go", height = "2", width = "30", command = paraclick).pack()
  Button(screenparabola, text = "RETURN TO HOMEPAGE", height = "2", width = "30", command = delete3).pack()



  
##def ParabolaBut():
##  global screenparabola
##  screenparabola = Toplevel(screenloop)
##  screenparabola.title("Parabola")
##  screenparabola.geometry("1080x720")
##  Label(screenparabola, text = "Graphs with Matpltlib", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
##  Button(screenparabola, text = "PARABOLA STANDARD EQUATION", height = "2", width = "30", command = CalulatePrbo).pack()
##  Button(screenparabola, text = "PARABOLA EXPANDED EQUATION", height = "2", width = "30", command = EllipseBut).pack()
##  Button(screenparabola, text = "RETURN TO HOMEPAGE", height = "2", width = "30", command = Homescreen).pack()
##

##def CalulatePrbo():
##    global testscreen
##    testscreen = Toplevel(screenloop)
##    print('testing')
##    print('Parabola in standard equation')
##    test = StringVar()
##    test_entry = Entry(testscreen, textvariable = test)
##    test_entry.pack()
##    a = int(test)
##    
##    parabola = (y**2 - 4*a*x)
##    axes()
##    mpl.contour(x, y, parabola, [0], colors='k')
##    mpl.show()
##
##    fig = Figure(figsize=(5, 4), dpi=100)
##    t = np.arange(0, 3, .01)
##    fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
##
##    canvas = FigureCanvasTkAgg(fig, master=screenparabola)  # A tk.DrawingArea.
##    canvas.draw()
##    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
##
##    toolbar = NavigationToolbar2Tk(canvas, screenparabola)
##    toolbar.update()
##    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

ellipsedrop = ["(Select)","Ellipse STANDARD EQUATION", "Ellipse EXPANDED EQUATION"]


def elipclick( event ):
    if ellipsecombo.get() == "Ellipse STANDARD EQUATION" :
        h = IntVar ()
        k = IntVar ()
        Label(screenellipse, text ="Please enter the value of h").pack()
        Entry(screenellipse, textvariable = h)
        Label(screenellipse, text ="Please enter the value of k").pack()
        Entry(screenellipse, textvariable = k)
        Button(screenellipse, command = elipstd )
        def elipstd():
            t = np.linspace(0,2*np.pi, 1000)
            p = h + a*np.cos(t)
            q = k + b*np.sin(t)
            mpl.axis('equal')
            mpl.grid()
            mpl.plot(p,q)
            mpl.show()
            
    elif ellipsecombo.get() == "Ellipse EXPANDED EQUATION" :
        a = IntVar ()
        Label(screenellipse, text ="Please enter the value of A").pack()
        Entry(screenellipse, textvariable = a)
        
        b = IntVar ()
        Label(screenellipse, text ="Please enter the value of B").pack()
        Entry(screenellipse, textvariable = a)
        
        c = IntVar ()
        Label(screenellipse, text ="Please enter the value of C").pack()
        Entry(screenellipse, textvariable = a)
        
        f = IntVar ()
        Label(screenparabola, text ="Please enter the value of F").pack()
        Entry(screenparabola, textvariable = a)
        
        g= IntVar ()
        Label(screenparabola, text ="Please enter the value of G").pack()
        Entry(screenparabola, textvariable = a)

        h = IntVar ()
        Label(screenparabola, text ="Please enter the value of H").pack()
        Entry(screenparabola, textvariable = h)
        Button(screenparabola, command = paraexpd )

        def paraexpd ():
            #Defining values for x and y
            x = np.linspace(-50, 51, 200)
            y = np.linspace(-50, 51, 200)
            #meshgrid makes an array, this is useful in defining functions
            x, y = np.meshgrid(x, y)

            axes()
            mpl.contour(x, y,(a*x**2 + h*x*y + b*y**2 + g*x + f*y + c), [0], colors='k')
            mpl.show()

def EllipseBut():
  global screenellipse
  print('EllipseBut Working')
  screenellipse = Toplevel(screenloop)
  screenellipse.title("Ellipse")
  screenellipse.geometry("720x720")
  Label(screenellipse, text = "Graphs with Matpltlib", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  ellipsecombo = ttk.Combobox(screenellipse,value = ellipsedrop)
  ellipsecombo.current(0)
  ellipsecombo.bind('<<ComboBoxSelected >>', elipclick)
  ellipsecombo.pack()  
  

  Button(screenellipse, text = "RETURN TO HOMEPAGE", height = "2", width = "30", command = delete4).pack()



##def EllipseBut():
##  global screenellipse
##  print('HyperbolaBut Working')
##  screenellipse = Toplevel(screenloop)
##  screenellipse.title("Ellipse")
##  screenellipse.geometry("1080x720")
##  Label(screenellipse, text = "Graphs with Matpltlib", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
##  Button(screenellipse, text = "Ellipse STANDARD EQUATION", height = "2", width = "30", command = ParabolaBut).pack()
##  Button(screenellipse, text = "Ellipse EXPANDED EQUATION", height = "2", width = "30", command = EllipseBut).pack()
##  Button(screenellipse, text = "RETURN TO HOMEPAGE", height = "2", width = "30", command = Homescreen).pack()


Hyperdrop = ["(Select)","HYPERBOLA STANDARD EQUATION", "HYPERBOLA EXPANDED EQUATION"]
def hyperclick( event ):
    if hypercombo.get() == "HYPERBOLA STANDARD EQUATION" :
        a = IntVar ()
        b = IntVar ()
        Label(screenhyperbola, text ="Please enter the value of a").pack()
        Entry(screenhyperbola, textvariable = a)
        Label(screenhyperbola, text ="Please enter the value of b").pack()
        Entry(screenhyperbola, textvariable = b)
        Button(screenhyperbola, command = hyperstd )
        def hyperstd():
            axes()
            hyperbola = (q**2/a**2 - w**2/b**2)
            mpl.contour(q, w,hyperbola, [1], colors='k')

            mpl.axis('equal')
            mpl.grid()
            mpl.plot(p,q)
            mpl.show()
            
    elif paracombo.get() == "Ellipse EXPANDED EQUATION" :
        a = IntVar ()
        Label(screenellipse, text ="Please enter the value of A").pack()
        Entry(screenellipse, textvariable = a)
        
        b = IntVar ()
        Label(screenellipse, text ="Please enter the value of B").pack()
        Entry(screenellipse, textvariable = a)
        
        c = IntVar ()
        Label(screenellipse, text ="Please enter the value of C").pack()
        Entry(screenellipse, textvariable = a)
        
        f = IntVar ()
        Label(screenparabola, text ="Please enter the value of F").pack()
        Entry(screenparabola, textvariable = a)
        
        g= IntVar ()
        Label(screenparabola, text ="Please enter the value of G").pack()
        Entry(screenparabola, textvariable = a)

        h = IntVar ()
        Label(screenparabola, text ="Please enter the value of H").pack()
        Entry(screenparabola, textvariable = h)
        Button(screenparabola, command = paraexpd )

        def hyperexpd ():
            #Defining values for x and y
            q = np.linspace(-100, 101, 200)
            w = np.linspace(-100, 101, 200)
            q, w = np.meshgrid(q, w)


            axes()
            mpl.contour(q,w,(a*x**2 + h*x*y + b*y**2 + g*x + f*y + c), [0], colors='k')
            mpl.show()



def HyperbolaBut():
  global screenhyperbola
  print('HyperbolaBut Working')
  screenhyperbola = Toplevel(screenloop)
  screenhyperbola.title("Hyperbola")
  screenhyperbola.geometry("720x720")
  Label(screenhyperbola, text = "Graphs with Matpltlib", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  hypercombo = ttk.Combobox(screenhyperbola,value = Hyperdrop)
  hypercombo.current(0)
  hypercombo.bind('<<ComboBoxSelected >>', hyperclick)
  hypercombo.pack()  
  Button(screenhyperbola, text = "RETURN TO HOMEPAGE", height = "2", width = "30", command = delete5).pack()



##
##def HyperbolaBut():
##  global screenhyperbola
##  print('HyperbolaBut Working')
##  screenhyperbola = Toplevel(screenloop)
##  screenhyperbola.title("Hyperbola")
##  screenhyperbola.geometry("1080x720")
##  Label(screenhyperbola, text = "Graphs with Matpltlib", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
##  Button(screenhyperbola, text = "Hyperbola STANDARD EQUATION", height = "2", width = "30", command = ParabolaBut).pack()
##  Button(screenhyperbola, text = "Hyperbola EXPANDED EQUATION", height = "2", width = "30", command = EllipseBut).pack()
##  Button(screenhyperbola, text = "RETURN TO HOMEPAGE", height = "2", width = "30", command = Homescreen).pack()
##

def Homescreen():
  global screenloop
  
  print('main_screen Working')
  screenloop = Tk()
  ##screenloop = Toplevel(screen)
  photo = PhotoImage(file = r"images.png")
  ##labelphoto = Label(screenloop, image = photo)
  ##labelphoto.pack()
  screenloop.title("MainScreen")
  screenloop.geometry("1080x720")
  Label(text = "Graphs with Matpltlib", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Button(text = "Straight Lines", height = "2", width = "30", command = StraightBut).pack()
  Button(text = "PARABOLA", height = "2", width = "30", command = ParabolaBut).pack()
  Button(text = "ELLIPSE", height = "2", width = "30", command = EllipseBut).pack()
  Button(text = "HYPERBOLA", height = "2", width = "30", command = HyperbolaBut).pack()
  Button(text = "TrigoFunctions", height = "2", width = "30", command = Trigo).pack()

  screenloop.mainloop()

Homescreen()
















































