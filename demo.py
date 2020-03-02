# exercice carte

import tkinter

import webbrowser


# fonctions
def ma_page():
    webbrowser.open_new("https://www.facebook.com/cyrille42blekou")


# personnalisé
app = tkinter.Tk()
app.title("mon app")
app.config(bg="#550000")
app.iconbitmap("1.ico")
app.geometry("800x600")


# la boite
frame = tkinter.Frame(app, bg="#550000")


# widgets
label1 = tkinter.Label(frame, text="Bienvenus sur ma super app",
                       bg="#550000", font=("Fredoka One", 40), fg="#fff")
label1.pack()


label2 = tkinter.Label(frame, text="yo les amis c'est cycy",
                       bg="#550000", font=("Fredoka One", 20), fg="#fff")
label2.pack()

# affichage de la boite
frame.pack(expand="yes")

# button
fb_button = tkinter.Button(frame, text="ouvrir ma page facebook", bg="#fff", font=(
    "Fredoka One", 20), fg="#550000", command=ma_page)
fb_button.pack()


# affichage
app.mainloop()
