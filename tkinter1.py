import tkinter as tk 

root = tk.Tk()
root.title("Tkinter")
root.geometry("300x300")

label = tk.Label(root, text="hello", font=("Arial",14))
label.pack(pady=10)

button = tk.Button(root, text="click", font=("Arial",12),bg="black",fg="white")
button.pack()

entry = tk.Entry(root, font=("Arial",14),width=20)
entry.pack()

frame =tk.Frame(root ,bg="lightblue",padx=10,pady=10)
frame.pack(pady=10)

label1 = tk.Label(frame, text="label in frame",font=("14"))
label1.pack()

radiobutton = tk.Radiobutton(root, text = "Επιλογη 1",font=("Arial",14))
radiobutton.pack()

checkbutton = tk.Checkbutton(root, text="Kαφεs")
checkbutton.pack()

text_box =tk.Text(root, font=("Arial",14),height=5, width=20)
text_box.pack()

root.mainloop()