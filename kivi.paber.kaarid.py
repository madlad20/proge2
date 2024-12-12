# Import Required Library
from tkinter import *
import random

# Create Object
root = Tk()

# Set geometry
root.geometry("720x480")

# Set title
root.title("Kivi paber käärid")

# Computer Value
computer_value = {
	"0": "Kivi",
	"1": "Paber",
	"2": "Käärid"
}

# Reset The Game


def reset_game():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	l1.config(text="Player			 ")
	l3.config(text="Computer")
	l4.config(text="")

# Disable the Button


def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"

# If player selected rock


def isrock():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Kivi":
		match_result = "Viik"
	elif c_v == "Käärid":
		match_result = "Mängja võit"
	else:
		match_result = "Arvuti võit"
	l4.config(text=match_result)
	l1.config(text="Kivi		 ")
	l3.config(text=c_v)
	button_disable()

# If player selected paper


def ispaper():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Paber":
		match_result = "Viik"
	elif c_v == "Käärid":
		match_result = "Arvuti võit"
	else:
		match_result = "Mängija võit"
	l4.config(text=match_result)
	l1.config(text="Paber		 ")
	l3.config(text=c_v)
	button_disable()

# If player selected scissor


def isscissor():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Kivi":
		match_result = "Arvuti võit"
	elif c_v == "Käärid":
		match_result = "Viik"
	else:
		match_result = "Mängija võit"
	l4.config(text=match_result)
	l1.config(text="Käärid		 ")
	l3.config(text=c_v)
	button_disable()


# Add Labels, Frames and Button
Label(root,
	text="Kivi Paber Käärid",
	font="normal 20 bold",
	fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame,
		text="Mängija			 ",
		font=10)

l2 = Label(frame,
		text="VS			 ",
		font="normal 10 bold")

l3 = Label(frame, text="Arvuti", font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root,
		text="",
		font="normal 20 bold",
		bg="white",
		width=15,
		borderwidth=2,
		relief="solid")
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Kivi",
			font=10, width=7,
			command=isrock)

b2 = Button(frame1, text="Paber ",
			font=10, width=7,
			command=ispaper)

b3 = Button(frame1, text="Käärid",
			font=10, width=7,
			command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(root, text="Restart",
	font=10, fg="red",
	bg="black", command=reset_game).pack(pady=20)

# Execute Tkinter
root.mainloop()
