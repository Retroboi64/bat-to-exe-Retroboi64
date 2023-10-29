#By Retroboi64
import customtkinter
import tkinter as tk
import customtkinter as CTK
import tkinter.filedialog as filedialog
import subprocess



def help_window():
    help_label_text = "Batoexe is a bat to exe coverter\nBy Retroboi64"
    help_window = customtkinter.CTk()
    help_window.title("Help")
    help_window.geometry("200x100")
    help_window.resizable(False, False)
    help_window.iconbitmap("batoexe.ico")

    help_label = customtkinter.CTkLabel(help_window, text=help_label_text)
    help_label.pack()

    help_window.mainloop()
    

def open_selected_bat():
    file_path = filedialog.askopenfilename(filetypes=[("Batch files", "*.bat")])
    if file_path:
        subprocess.run(['batoexe.bat', file_path], shell=True)
        quit()


root = customtkinter.CTk()
root.title("batoexe")
root.geometry("200x130")
root.resizable(False, False)
root.iconbitmap("batoexe.ico")

frame = customtkinter.CTkFrame(root)
frame.pack()

label = customtkinter.CTkLabel(frame, text="Open a batch file")
label.pack()

label2 = customtkinter.CTkLabel(frame, text="by Retroboi64")
label2.pack(side ="top")

help = customtkinter.CTkButton(frame, text="Help", command=help_window)
help.pack(side = ('bottom'))

button = customtkinter.CTkButton(frame, text="Open", command=open_selected_bat)
button.pack(side = ('bottom'))


root.mainloop()
