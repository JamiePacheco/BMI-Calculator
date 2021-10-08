from tkinter import *


app = Tk()
app.title("BMI CALCULATOR")
app.geometry("250x150")
app.config(bg = "grey")

BMI = DoubleVar()
W = IntVar()
Math = StringVar()
MetricBMI = IntVar()
ImperialBMI = IntVar()

def BMI_Calculations(i):

    global Math

    if i == 1:     
        Math = "Metric"
    elif i == 2:
        Math = "Imperial"

def Calculating_BMI(w, h):

    def Getting_BMI():
        global MetricBMI
        global ImperialBMI

        if Math == "Metric":
            MetricBMI = round(int(w)/(int(h)**2), 2)
            BMI.set(MetricBMI)
            BMI_Display.delete(0,END)
            BMI_Display.insert(0, str(BMI.get()))

        elif Math == "Imperial":
            ImperialBMI = round((703*int(w))/(int(h)**2), 2)
            BMI.set(ImperialBMI)
            BMI_Display.delete(0,END)
            BMI_Display.insert(0, str(BMI.get()))

    def Getting_Class():
        if BMI.get() < 18.5:
            Class_Display.delete(0,END)
            Class_Display.insert(0,"UNDERWEIGHT")
        elif BMI.get() >= 18.5 and BMI.get() < 25:
            Class_Display.delete(0,END)
            Class_Display.insert(0,"AVERAGE")
        elif BMI.get() >= 25 and BMI.get() < 30:
            Class_Display.delete(0,END)
            Class_Display.insert(0,"OVERWEIGHT")
        elif BMI.get() > 30:
            Class_Display.delete(0,END)
            Class_Display.insert(0,"OBESE")

    Getting_BMI()
    Getting_Class()

def clear_function():
    Height_Entry.delete(0,END)
    Weight_Entry.delete(0,END)
    BMI_Display.delete(0,END)
    Class_Display.delete(0,END)
    

Radiobutton(app, text="METRIC", variable=W, value=1, bg = "grey",command = lambda: BMI_Calculations(W.get())).grid(column=1, row=0)
Radiobutton(app, text="IMPERIAL", variable=W, value=2, bg = "grey", command = lambda: BMI_Calculations(W.get())).grid(column=2, row=0)

Weight_Label = Label(app, text = "ENTER YOUR WEIGHT:", bg="grey").grid(column=1, row=1)
Weight_Entry = Entry(app)
Weight_Entry.grid(column=2, row=1)

Height_Label = Label(app, text = "ENTER YOUR HEIGHT:",bg="grey").grid(column=1, row=2)
Height_Entry = Entry(app)
Height_Entry.grid(column=2, row=2)

Calculate_Button = Button(app, text = "CALCULATE",bg="dark grey", padx=15,pady=5, command = lambda: Calculating_BMI(Weight_Entry.get(), Height_Entry.get())).grid(column=1,row=3)
Clear_Button = Button(app, text="CLEAR",bg="dark grey",padx=25,pady=5,command = clear_function).grid(column=2,row=3)


BMI_Label = Label(app, text = "YOUR BMI IS:",bg="grey").grid(column=1, row=4)
BMI_Display = Entry(app)
BMI_Display.grid(column=2,row=4)

Class_Label = Label(app, text = "YOU ARE:", bg="grey").grid(column=1,row=5)
Class_Display = Entry(app)
Class_Display.grid(column=2,row=5)




app.mainloop()