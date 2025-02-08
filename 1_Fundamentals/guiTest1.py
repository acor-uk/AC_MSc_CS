import tkinter as tk

# Function to open the test alert window
def testAlert():
    # Create the test alert window
    testAlertWindow = tk.Toplevel() #create a new window
    testAlertWindow.title("Test Alert") #set the title of the window
    testAlertWindow.geometry("200x100+600+400") #set the size of the window
    # Add a label to display the message
    testAlertLabel = tk.Label(testAlertWindow, text="Hello World!") #create a label
    testAlertLabel.pack(pady=10) #pack the label to the window
    # Add a button to close the window
    testAlertButton = tk.Button(testAlertWindow, text="Close", command=testAlertWindow.destroy) #create a button
    testAlertButton.pack() #pack the button to the window

# Create the main window
window = tk.Tk() #create main window
window.title("Test Interface") # window title appears in the title bar
window.geometry("250x200+500+300") # set the size of window. tkinter receives parameters as strings

# Add a label to display the title of the application
testLabel = tk.Label(text="Test GUI", font=("Arial", 24)) #create a label, syntax is quite similar to c# winforms
testLabel.pack(pady=10)#pack the label to the window, pady is padding in y direction

# Add a button to open the AddTaskMenu window
test_btn = tk.Button(
    window,
    text="Test Me!",
    width=6,
    height=2,
    command=testAlert
)
test_btn.pack()

# Add a text field
test_text = tk.Text(window, height=10, width=100)
test_text.pack(pady=20)
# Start the tkinter event loop
window.mainloop()