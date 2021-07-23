from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

import back_end

window=Tk()
window.title("Contact Book")
window_width=700
window_height=400
window.geometry("700x400")
window.resizable(False,False)
window.config(bg="black")

#==========================Variables==========================
first_name=StringVar()
last_name=StringVar()
gender=StringVar()
address=StringVar()
contact= IntVar()

search=StringVar()

id=IntVar()

#==========================Functions==========================
def on_double_click():
    current_item=tree_view.focus()
    content=tree_view.item(current_item)

    item_selected=content["values"]

    # Set values in the field
    first_name.set(item_selected[1])
    last_name.set(item_selected[2])
    gender.set(item_selected[3])
    address.set(item_selected[4])
    contact.set(item_selected[5])


def display_data():
    #clear current data  
    tree_view.delete(*tree_view.get_children())
    data=back_end.view()

    for i in data:
        tree_view.insert("","end",values=(i))
        tree_view.bind("<Double-1>",on_double_click)


def search_data():
    if search.get()!="":
        #clearing current display data
        tree_view.delete(*tree_view.get_children())
        data=back_end.search(search.get())
        if data==[]:
            tkMessageBox.showinfo("Message","No contact with {} exists".format(str(search.get())))
        else:
            for i in data:
                tree_view.insert("","end",values=(i))


def delete_data():
    if not tree_view.selection():
        tkMessageBox.showwarning("Warning","Select a contact to delete")
    else:
        ask=tkMessageBox.askquestion("Confirm","Are you sure you want to delete this record?",icon="warning")
        if ask=="yes":
            current_item=tree_view.focus()
            content=tree_view.item(current_item)

            item_selected=content["values"]

            back_end.delete(item_selected[0])
            tree_view.delete(current_item)



def update_data():
    if  first_name.get() == "" or last_name.get() == "" or gender.get() == "" or address.get() == "" or  contact.get() == "":
        result = tkMessageBox.showwarning('', 'Please Fill The Required Field!!!', icon="warning")
    else:
        # Update in DB
        back_end.update(id.get(),first_name.get(),last_name.get(),gender.get(),address.get(),contact.get())
        tkMessageBox.showinfo("Message","Contact updated successfully")
        first_name.set("")
        last_name.set("")
        gender.set("")
        address.set("")
        contact.set("")
    display_data()

# Create new window to update entry in contact book
def update_entry():
    if not tree_view.selection():
        tkMessageBox.showwarning("Warning","Select a contact to update")
    else:
        current_item=tree_view.focus()
        content=tree_view.item(current_item)

        item_selected=content["values"]

        # Set values in the field
        id.set(item_selected[0])
        first_name.set(item_selected[1])
        last_name.set(item_selected[2])
        gender.set(item_selected[3])
        address.set(item_selected[4])
        contact.set(item_selected[5])

        update_entry_window=Toplevel()
        update_entry_window.title("Update Contact")
        update_entry_window.geometry("330x300")
        update_entry_window.resizable(False,False)
        update_entry_window.config(bg="#15244C")

        # Add widgets for new window
        f_name_label=Label(update_entry_window, text="First Name", font=("Arial", 12),bg="#15244C", fg="white")
        f_name_label.grid(row=0, pady=10, sticky=W)
        f_name_entry=Entry(update_entry_window, textvariable=first_name, font=('arial', 14))
        f_name_entry.grid(row=0, column=1, pady=10)

        l_name_label=Label(update_entry_window, text="Last Name", font=("Arial", 12),bg="#15244C", fg="white")
        l_name_label.grid(row=1, pady=10, sticky=W)
        l_name_entry=Entry(update_entry_window, textvariable=last_name, font=('arial', 14))
        l_name_entry.grid(row=1, column=1, pady=10)

        gender_new_label=Label(update_entry_window, text="Gender", font=("Arial", 12),bg="#15244C",fg="white")
        gender_new_label.grid(row=2, pady=10, sticky=W)

        radio_group=Frame(update_entry_window,bg="gray")
        male=Radiobutton(radio_group, text="Male", variable=gender, value="Male", font=('arial', 14), bg="#15244C", fg="cyan")
        male.pack(side=LEFT)
        female=Radiobutton(radio_group, text="Female", variable=gender, value="Female", font=('arial', 14), bg="#15244C", fg="cyan")
        female.pack(side=LEFT)
        radio_group.grid(row=2, column=1, pady=10)
    
        address_new_label=Label(update_entry_window, text="Address", font=("Arial", 12),bg="#15244C",fg="white")
        address_new_label.grid(row=3, pady=10, sticky=W)
        address_new_entry=Entry(update_entry_window, textvariable=address, font=('arial', 14))
        address_new_entry.grid(row=3, pady=10, column=1)

        contact_new_label=Label(update_entry_window, text="Contact No.", font=("Arial", 12),bg="#15244C",fg="white")
        contact_new_label.grid(row=4, pady=10, sticky=W)
        contact_new_entry=Entry(update_entry_window, textvariable=contact, font=('arial', 14))
        contact_new_entry.grid(row=4, pady=10, column=1)

        update_button=Button(update_entry_window, text="Update", width=44, command=update_data)
        update_button.grid(row=5, columnspan=2, padx=5, pady=10)

# Add new data to database
def add_data():
    if  first_name.get() == "" or last_name.get() == "" or gender.get() == "" or address.get() == "" or  contact.get() == "":
        result = tkMessageBox.showwarning('', 'Please Fill The Required Field!!!', icon="warning")
    else:
        # Add in DB
        back_end.insert(first_name.get(),last_name.get(),gender.get(),address.get(),contact.get())
        tkMessageBox.showinfo("Message","Contact added successfully")
        first_name.set("")
        last_name.set("")
        gender.set("")
        address.set("")
        contact.set("")
    display_data()

# Create new window to add entry in contact book
def add_new_entry():
    global add_entry_window
    first_name.set("")
    last_name.set("")
    gender.set("")
    address.set("")
    contact.set(0)

    add_entry_window=Toplevel()
    add_entry_window.title("Add New Contact")
    add_entry_window.geometry("330x300")
    add_entry_window.resizable(False,False)
    add_entry_window.config(bg="#15244C")

    # Add widgets for new window
    first_name_label=Label(add_entry_window, text="First Name", font=("Arial", 12),bg="#15244C", fg="white")
    first_name_label.grid(row=0, pady=10, sticky=W)
    first_name_entry=Entry(add_entry_window, textvariable=first_name, font=('arial', 14))
    first_name_entry.grid(row=0, column=1, pady=10)

    last_name_label=Label(add_entry_window, text="Last Name", font=("Arial", 12),bg="#15244C", fg="white")
    last_name_label.grid(row=1, pady=10, sticky=W)
    last_name_entry=Entry(add_entry_window, textvariable=last_name, font=('arial', 14))
    last_name_entry.grid(row=1, column=1, pady=10)

    gender_label=Label(add_entry_window, text="Gender", font=("Arial", 12),bg="#15244C",fg="white")
    gender_label.grid(row=2, pady=10, sticky=W)

    radio_group=Frame(add_entry_window,bg="gray")
    male=Radiobutton(radio_group, text="Male", variable=gender, value="Male", font=('arial', 14), bg="#15244C", fg="cyan")
    male.pack(side=LEFT)
    female=Radiobutton(radio_group, text="Female", variable=gender, value="Female", font=('arial', 14), bg="#15244C", fg="cyan")
    female.pack(side=LEFT)
    radio_group.grid(row=2, column=1, pady=10)
    
    address_label=Label(add_entry_window, text="Address", font=("Arial", 12),bg="#15244C",fg="white")
    address_label.grid(row=3, pady=10, sticky=W)
    address_entry=Entry(add_entry_window, textvariable=address, font=('arial', 14))
    address_entry.grid(row=3, pady=10, column=1)

    contact_label=Label(add_entry_window, text="Contact No.", font=("Arial", 12),bg="#15244C",fg="white")
    contact_label.grid(row=4, pady=10, sticky=W)
    contact_entry=Entry(add_entry_window, textvariable=contact, font=('arial', 14))
    contact_entry.grid(row=4, pady=10, column=1)

    add_button=Button(add_entry_window, text="Add", width=44, command=add_data)
    add_button.grid(row=5, columnspan=2, padx=5, pady=10)

#==========================Frames==========================
top_frame=Frame(window, width=500, bd=1, relief=SOLID)
top_frame.pack(side=TOP)

title_label=Label(top_frame,text="Contact Management System", font=('arial', 16), width=500)
title_label.pack(fill=X)

# Add widgets
widgets_frame = Frame(window, width=500,bg="#0B4670")
widgets_frame.pack(side=LEFT, fill=Y)

add_button=Button(widgets_frame, text="Add New Contact", bg="cyan", command=add_new_entry)
add_button.pack(side=TOP, padx=10, pady=10, fill=X)

view_button=Button(widgets_frame, text="View All", bg="cyan", command=display_data)
view_button.pack(side=TOP, padx=10, pady=10, fill=X)

search_box_label=Label(widgets_frame, text="Enter First Name", font=('verdana', 10),bg="#0B4670")
search_box_label.pack()

search_box_entry=Entry(widgets_frame,textvariable=search, font=('verdana', 15), width=10)
search_box_entry.pack(side=TOP, padx=10, fill=X)

search_button=Button(widgets_frame, text="Search", bg="cyan", command=search_data)
search_button.pack(side=TOP, padx=10, pady=10, fill=X)

update_label=Label(widgets_frame, text="Select a contact to \nupdate/delete", font=('verdana', 10),bg="#0B4670")
update_label.pack()

update_button=Button(widgets_frame, text="Update", bg="cyan", command=update_entry)
update_button.pack(side=TOP, padx=10, pady=10, fill=X)

delete_button=Button(widgets_frame, text="Delete", bg="cyan", command=delete_data)
delete_button.pack(side=TOP, padx=10, pady=10, fill=X)


# Display frame
display_frame= Frame(window, width=500)
display_frame.pack(side=RIGHT)

scrollbarx = Scrollbar(display_frame, orient=HORIZONTAL)
scrollbary = Scrollbar(display_frame, orient=VERTICAL)
tree_view = ttk.Treeview(display_frame, columns=("id", "first_name", "last_name", "gender", "address", "contact"), height=400,selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree_view.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree_view.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree_view.heading("id", text="ID", anchor=W)
tree_view.heading('first_name', text="First Name", anchor=W)
tree_view.heading('last_name', text="Last Name", anchor=W)
tree_view.heading('gender', text="Gender", anchor=W)
tree_view.heading('address', text="Address", anchor=W)
tree_view.heading('contact', text="Contact Number", anchor=W)

tree_view.column('#0', stretch=NO, minwidth=0, width=0)
tree_view.column('#1', stretch=NO, minwidth=0, width=0)
tree_view.column('#2', stretch=NO, minwidth=0, width=80)
tree_view.column('#3', stretch=NO, minwidth=0, width=80)
tree_view.column('#4', stretch=NO, minwidth=0, width=90)
tree_view.column('#5', stretch=NO, minwidth=0, width=160)
tree_view.column('#6', stretch=NO, minwidth=0, width=160)

tree_view.pack()

#display_data()




#==========================Initialization==========================
if __name__=="__main__":
    window.mainloop()
