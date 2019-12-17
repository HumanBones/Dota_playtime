import tkinter as tk
import scrap

WIDTH = 600
HEIGHT = 800

def test_func():
    txt = scrap.urls()
    #print(txt)
    label['text'] ="Darko:  " + txt[0] + "\nMiksi:  " + txt[1]


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='dota.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='#99bbff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

main_label = tk.Label(frame, font=40,text='Darko v Miksi')
main_label.place(relwidth=0.5, relheight=1)
#entry = tk.Entry(frame, font= 40)
#entry.place(relwidth=0.5, relheight=1)

button = tk.Button(frame,text = 'Get Data', font=40, command=lambda: test_func())
button.place(relx=0.7, relheight=1,relwidth=0.3)

lower_frame = tk.Frame(root, bg='#99bbff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font= 40)
label.place(relwidth=1,relheight=1)

root.mainloop()


#For exporting to .exe file --> #pyinstaller.exe --onefile --icon=icon.png -w main.py

