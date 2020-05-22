
import tkinter as tk 
from tkinter import ttk
win = tk.Tk()
win.title('Label Frame ')

label_frame = ttk.LabelFrame(win, text='Enter your details below ')
label_frame.grid(row=0, column=0, padx=40)

labels = ['What is your name : ' , 'What is your age ', 'What is your gender : ', 'Country : ', 'State : ', 'City : ', 'address']

for i in range(len(labels)):
    cur_label = 'label' + str(i) # label0, label1
    cur_label = ttk.Label(label_frame, text = labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W)

name_var = tk.StringVar() 
user_info = {
    'name': tk.StringVar(),
    'age': tk.StringVar(),
    'gender': tk.StringVar(),
    'country': tk.StringVar(),
    'state': tk.StringVar(),
    'city': tk.StringVar(),
    'address' : tk.StringVar()
}
counter=0
for i in user_info:
    cur_entrybox = 'entry' + i # entryname # entryage
    cur_entrybox = ttk.Entry(label_frame, width=20, textvariable=user_info[i])
    cur_entrybox.grid(column=1, row=counter)
    counter += 1 

def submit():
    l=[]
    for i in user_info:
        l.append(user_info[i].get())

    print(l)

submit_btn = ttk.Button(win, text='Submit', command=submit)
submit_btn.grid(row=1, columnspan=2)

for child in label_frame.winfo_children():
    child.grid_configure(padx=40, pady=10)

label_frame1 = ttk.LabelFrame(win, text='Enter your details below ')
label_frame1.grid(row=0, column=4, padx=40)

labels = ['What is your name : ' , 'What is your age ', 'What is your gender : ', 'Country : ', 'State : ', 'City : ', 'address']

for i in range(len(labels)):
    cur_label = 'label' + str(i) # label0, label1
    cur_label = ttk.Label(label_frame1, text = labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W)

name_var = tk.StringVar() 
user_info = {
    'name': tk.StringVar(),
    'age': tk.StringVar(),
    'gender': tk.StringVar(),
    'country': tk.StringVar(),
    'state': tk.StringVar(),
    'city': tk.StringVar(),
    'address' : tk.StringVar()
}
counter=0
for i in user_info:
    cur_entrybox = 'entry' + i # entryname # entryage
    cur_entrybox = ttk.Entry(label_frame1, width=20, textvariable=user_info[i])
    cur_entrybox.grid(column=1, row=counter)
    counter += 1 

def submit1():
    l=[]
    for i in user_info:
        l.append(user_info[i].get())

    print(l)

submit_btn = ttk.Button(win, text='Submit', command=submit1)
submit_btn.grid(row=1, column=4)

for child in label_frame1.winfo_children():
    child.grid_configure(padx=40, pady=10)

win.mainloop()