# import all functions from the tkinter
from tkinter import *
import datetime
# import messagebox class from tkinter
from tkinter import messagebox
from agecalculator import agecalculator

# Function for clearing the
# contents of all text entry boxes

def clearAll() :

	# deleting the content from the entry box

	dayField.delete(0, END)
	monthField.delete(0, END)
	yearField.delete(0, END)
	rsltDayField.delete(0, END)
	rsltMonthField.delete(0, END)
	rsltYearField.delete(0, END)


# function to calculate Age
def calculateAge() :
    birth_day = int(dayField.get())
    birth_month = int(monthField.get())
    birth_year = int(yearField.get())
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


	# if error is occur then return
    if (dayField.get() == "" or monthField.get() == ""
		or yearField.get() == "") :
        messagebox.showerror("Input Error")
        clearAll()
        return -1
		
    elif (birth_day < 0 or birth_month < 0 or birth_year < 0):
        messagebox.showerror("Enter Correct date")
        clearAll()
        return -1
    
    elif (birth_month>12 or birth_day > month[birth_month+1]):
        messagebox.showerror("Enter correct date")
        clearAll()
        return -1
    else :
        cal_age=agecalculator(birth_day, birth_month, birth_year, month[birth_month-1])
        rsltDayField.insert(10, str(cal_age.get_days()))
        rsltMonthField.insert(10, str(cal_age.get_months()))
        rsltYearField.insert(10, str(cal_age.get_years()))
# Driver Code
if __name__ == "__main__" :

	# Create a GUI window
	gui = Tk()

	# Set the background colour of GUI window
	#gui.configure(background = "light green")

	# set the name of tkinter GUI window
	gui.title("Age Calculator")

	# Set the configuration of GUI window
	gui.geometry("325x260")

	# Create a Date Of Birth : label
	dob = Label(gui, text = "Date Of Birth")
	your_age = Label(gui, text = "Your Age")

	# Create a Day : label
	day = Label(gui, text = "Day")

	# Create a Month : label
	month = Label(gui, text = "Month")

	# Create a Year : label
	year = Label(gui, text = "Year")

	# Create a Years : label
	rsltYear = Label(gui, text = "Years")

    # Create a Months : label
	rsltMonth = Label(gui, text = "Months")

    # Create a Days : label
	rsltDay = Label(gui, text = "Days")

	# Create a Resultant Age Button and attached to calculateAge function
	resultantAge = Button(gui, text = "Resultant Age", fg = "Black", command = calculateAge)

	# Create a Clear All Button and attached to clearAll function
	clearAllEntry = Button(gui, text = "Clear All", fg = "Black", command = clearAll)

	# Create a text entry box for filling or typing the information.
	dayField = Entry(gui)
	monthField = Entry(gui)
	yearField = Entry(gui)


	rsltYearField = Entry(gui)
	rsltMonthField = Entry(gui)
	rsltDayField = Entry(gui)


	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	dob.grid(row = 0, column = 4)
	your_age.grid(row=8, column=3)

	day.grid(row = 1, column = 3)
	dayField.grid(row = 1, column = 4)

	month.grid(row = 2, column = 3)
	monthField.grid(row = 2, column = 4)

	year.grid(row = 3, column = 3)
	yearField.grid(row = 3, column = 4)
	resultantAge.grid(row = 4, column = 3)
	clearAllEntry.grid(row = 4, column = 4)
	rsltYear.grid(row = 9, column = 4)
	rsltYearField.grid(row = 9, column = 3)
	rsltMonth.grid(row = 10, column = 4)
	rsltMonthField.grid(row = 10, column = 3)
	rsltDay.grid(row = 11, column = 4)
	rsltDayField.grid(row = 11, column = 3)

	# Start the GUI
	gui.mainloop()
