import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("Multi-Launcher")
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        temp = f.read()
        temp = temp.split(',')
        apps = [x for x in temp if x.strip()]


def deleteApp(b):
    text = b['text']
    b.destroy()
    for app in apps:
        if app == text:
            apps.remove(app)



def addApp():
    for widget in inner_frame.winfo_children():
        widget.destroy()

    file_name = filedialog.askopenfilename(initialdir="/", title="Select File",
                                           filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(file_name)
    for app in apps:
        item = tk.Button(inner_frame, text=app, padx=10,
                         pady=5, fg="white", bg="#263D43")
        item['command'] = lambda b=item: deleteApp(b)
        item.pack()


def runApps():
    for app in apps:
        os.startfile(app)


outer_frame = tk.Canvas(root, height=700, width=700, bg="#263D42")

outer_frame.pack()

inner_frame = tk.Frame(root, bg="grey")
inner_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#263D42",  command=addApp)
openFile.pack()

run_a = tk.Button(root, text="Run Apps", padx=10,
                     pady=5, fg="white", bg="#263D42", command=runApps)


run_a.pack()

for app in apps:
    item = tk.Button(inner_frame, text=app, padx=10,
                     pady=5, fg="white", bg="#263D43")
    item['command'] = lambda b=item: deleteApp(b)
    item.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
