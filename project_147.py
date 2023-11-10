from tkinter import *

root = Tk()
root.title("ENCRYPTION WITH ASCII CODE")

root.geometry("400x400")
root.configure(background = "light blue")

entry_word = Entry(root)
entry_word.place(relx=0.5, rely=0.4, anchor=CENTER)

label = Label(root, text = "Name in ASCII : ", bg = "gold", fg = "black")
label2 = Label(root, text = "Encrypted Name : ", bg = "gold", fg = "black")

def asciiConverter():
    input_word = entry_word.get()
    
    for letter in input_word:
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label["text"] += str(ord(letter))
        label2["text"] += str(chr(encrypted))
        
btn = Button(root, text = "Display the ASCII code and the Encrypted value", command= asciiConverter, bg = "cyan", fg = "black")

btn.place(relx=0.5, rely=0.5, anchor=CENTER)
label.place(relx=0.5, rely=0.6, anchor=CENTER)
label2.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()

