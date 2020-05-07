# import all functions from the tkinter
from tkinter import *
# import messagebox class from tkinter
from tkinter import messagebox
from emicalculator import emicalculator


def reset() :
    """ Function for clearing the data """
	# deleting the content from the entry box
    prinicipalField.delete(0, END)
    interestField.delete(0, END)
    tenureField.delete(0, END)
    emiField.delete(0, END)
    totalAmountField.delete(0, END)
    totalInterestField.delete(0, END)
	

# function to calculate Age
def calculateEMI() :
    

	# if error is occur then return
    if (prinicipalField.get() == "" or interestField.get() == ""
		or tenureField.get() == "") :
        messagebox.showerror("Input Error")
        clearAll()
        return -1
	
    else :
        cal_emi=emicalculator(float(prinicipalField.get()),float(interestField.get()),float(tenureField.get()))
        emiField.insert(10, str(cal_emi.emi_value()))
        totalAmountField.insert(10, str(cal_emi.total_amount_value()))
        totalInterestField.insert(10, str(cal_emi.total_interest_value()))

if __name__ == "__main__" :

	# Create a window window
	window = Tk()

	# Set the background colour of window window
	#window.configure(background = "light green")

	# set the name of tkinter window window
	window.title("EMI Calculator")

	# Set the configuration of window window
	window.geometry("525x260")

	# Create a Loan details : label
	loan = Label(window, text = "Loan Details")
	result = Label(window, text = "Result")

	# Create a Principal amount : label
	prinicipal = Label(window, text = "Principal")

	# Create a Intrest : label
	interest = Label(window, text = "Interest")

	# Create a Moths : label
	tenure = Label(window, text = "Tenure (Months)")

	# Create a Emi value : label
	emi = Label(window, text = "EMI Value")

    # Create a Total Amount : label
	totalAmount = Label(window, text = "Total Amount")

    # Create a Total intreast : label
	totalInterest = Label(window, text = "Total Interest")

	# Create a CalculateEMII Button and attached to calculateAge function
	calculateEMI = Button(window, text = "CALCULATE", fg = "Black", command = calculateEMI)

	# Create Reset Button and attached to clearAll function
	resetAll = Button(window, text = "RESET", fg = "Black", command = reset)

	# Create a text entry box for filling or typing the information.
	prinicipalField = Entry(window)
	interestField = Entry(window)
	tenureField = Entry(window)


	emiField = Entry(window)
	totalAmountField = Entry(window)
	totalInterestField = Entry(window)


	# the widgets at respective positions
	# in table like structure .
	loan.grid(row = 0, column = 4)
	result.grid(row=0, column=7)
	

	prinicipal.grid(row = 1, column = 3)
	prinicipalField.grid(row = 1, column = 4)

	interest.grid(row = 2, column = 3)
	interestField.grid(row = 2, column = 4)

	tenure.grid(row = 3, column = 3)
	tenureField.grid(row = 3, column = 4)
	calculateEMI.grid(row = 5, column = 3)
	resetAll.grid(row = 5, column = 5)
	emi.grid(row = 1, column = 6)
	emiField.grid(row = 1, column = 7)
	totalAmount.grid(row = 2, column = 6)
	totalAmountField.grid(row = 2, column = 7)
	totalInterest.grid(row = 3, column = 6)
	totalInterestField.grid(row = 3, column = 7)

	# Start the window
	window.mainloop()
