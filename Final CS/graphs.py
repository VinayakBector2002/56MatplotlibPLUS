from tkinter import *
import matplotlib.pyplot as plt 
import numpy as np

def StraightBut():
    global screenstraight
    print('StraightBut Working')
    screenstraight = Toplevel(graphscreen)
    screenstraight.title("Straightlines")
    screenstraight.geometry("1080x720")
    Label(screenstraight, text = "Graphs with Matpltlib -- Straightlines", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    global straightlineX
    global straightlineY
    global straightlineK
 
    def delete2():
        screenstraight.destroy()
    def CalculateST():
        x = np.linspace(-60,61, 200)
        def axes():
            plt.grid()
            plt.axhline(0, alpha= .2, linewidth= 2, color='k' )
            #Printing Horizontal line, X axis
            plt.axvline(0, alpha= .2, linewidth= 2, color='k' )
        a = straightlineX.get()
        b = straightlineY.get()
        c = straightlineK.get()
        y = (a/b)*x+c
        eqn = str(a) + " x " +"+"+ str(b) + " y " +"+"+ str(c)+ " = 0"      
            #Printing Vertical line, Y axis
        plt.plot(x, y, '-r', label=eqn)
        plt.title('Graph of ' + eqn)
        
        plt.xlabel('x', color='#1C2833')
        
        plt.ylabel('y', color='#1C2833')
        
        plt.legend(loc='upper left')
        plt.plot(0,c)
        axes()
        plt.show()
    straightlineX = IntVar()
    straightlineY = IntVar()
    straightlineK = IntVar()

    Label(screenstraight, text = "Please enter details below").pack()
    Label(screenstraight, text = "Given equation ax + by + c= 0").pack()
    Label(screenstraight, text = "").pack()

    Label(screenstraight, text = "Coefficient of X, i.e a ").pack()
    straightlineX_entry = Entry(screenstraight, textvariable = straightlineX)
    straightlineX_entry.pack()
    Label(screenstraight, text = "").pack()

    Label(screenstraight, text = "Coefficient of Y, i.e b").pack()
    straightlineY_entry =  Entry(screenstraight, textvariable = straightlineY)
    straightlineY_entry.pack()

    Label(screenstraight, text = "Constant, i.e c").pack()
    straightlineK_entry = Entry(screenstraight, textvariable = straightlineK)
    straightlineK_entry.pack()
    Label(screenstraight, text = "").pack()

    Button(screenstraight, text = "Calculate", height = "2", width = "30", command = CalculateST).pack()
    Button(screenstraight, text = "back to homescreen",height = "2", width = "30", command = delete2).pack()

def Conics():
    return True
def Trigo():
    def axes():
        plt.grid()
        plt.axhline(0, alpha= .2, linewidth= 2, color='k' )
        #Printing Horizontal line, X axis
        plt.axvline(0, alpha= .2, linewidth= 2, color='k' )
        #Printing Vertical line, Y axis
        plt.axis('equal')
        for i in (-1*np.pi,1*np.pi,np.pi/2,-1*np.pi/2):
            plt.plot(i,0,'.')
        plt.axhline(1, alpha= .2, linewidth= 2, color='g' )
        plt.axhline(-1, alpha= .2, linewidth= 2, color='g' )
        
        plt.xlabel('Angle-Input')
        plt.ylabel('Integer-Output')
    def sin():
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        plt.plot(x, np.sin(x))
        plt.ylim(-5, 5)
        axes()
        plt.show()
    def cos():
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        plt.plot(x, np.cos(x))
        plt.ylim(-5, 5)
        axes()
        plt.show()
    def tan():
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        plt.plot(x, np.tan(x))
        plt.ylim(-5, 5)
        plt.grid()
        plt.axhline(0, alpha= .2, linewidth= 2, color='k' )
        #Printing Horizontal line, X axis
        plt.axvline(0, alpha= .2, linewidth= 2, color='k' )
        plt.show()
    def cot():
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        while True:
            try:
                plt.plot(x, 1/np.tan(x))
                plt.ylim(-5, 5)
            except:
                continue
            finally:
                break
        plt.grid()
        plt.axhline(0, alpha= .2, linewidth= 2, color='k' )
        #Printing Horizontal line, X axis
        plt.axvline(0, alpha= .2, linewidth= 2, color='k' )
        plt.show()
    def cosec():
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        while True:
            try:
                plt.plot(x, 1/np.sin(x))
                plt.ylim(-5, 5)
            except:
                continue
            finally:
                break
        axes()
        plt.show()
    def sec():
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        while True:
            try:
                plt.plot(x, 1/np.cos(x))
                plt.ylim(-5, 5)
            except:
                continue
            finally:
                break
        axes()
        plt.show()
    def tan2x():
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        plt.plot(x, np.tan(2*x))
        plt.ylim(-5, 5)
        plt.grid()
        plt.axhline(0, alpha= .2, linewidth= 2, color='k' )
        #Printing Horizontal line, X axis
        plt.axvline(0, alpha= .2, linewidth= 2, color='k' )
        plt.show()
    def sin2x():
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        plt.plot(x, np.sin(2*x))
        plt.ylim(-5, 5)
        axes()
        plt.show()
    def cos2x():
        x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
        plt.plot(x, np.cos(2*x))
        plt.ylim(-5, 5)
        axes()
        plt.show()
    screentrigo = Toplevel(graphscreen)
    screentrigo.title('TrigoFunctions')
    screentrigo.geometry("1080x720")
    Label(screentrigo, text = "Graphs with Matpltlib -- TrigoFunctions", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='sine',height = "2", width = "30", command = sin).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='Cos',height = "2", width = "30", command = cos).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='Tan',height = "2", width = "30", command = tan).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='Cot',height = "2", width = "30", command = cot).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='cosec',height = "2", width = "30", command = cosec).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='sec',height = "2", width = "30", command = sec).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='sin2x',height = "2", width = "30", command = sin2x).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='Cos2x',height = "2", width = "30", command = cos2x ).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='Tan2x',height = "2", width = "30", command = tan2x ).pack()
    Label(screentrigo, text = "").pack()
    Button(screentrigo, text ='Back to Homescreen',height = "2", width = "30",command= sin).pack()
    return True

def graphmain():
    global graphscreen
    graphscreen = Tk()
    graphscreen.title("Main")
    graphscreen.geometry("600x600")
    graphscreen['bg'] = '#A55D35'
    Label(graphscreen,text = "Conics with Matpltlib", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(graphscreen,text = "", bg = "#A55D35").pack()
    Button(graphscreen,text = "Straight Lines", height = "2", width = "30", command = StraightBut).pack()
    Label(graphscreen,text = "", bg = "#A55D35").pack()
    Button(graphscreen,text = "Conics", height = "2", width = "30", command = Conics).pack()
    Label(graphscreen,text = "", bg = "#A55D35").pack()
    Button(graphscreen,text = "TrigoFunctions", height = "2", width = "30", command = Trigo).pack()
    Label(graphscreen,text = "", bg = "#A55D35").pack()
graphmain()