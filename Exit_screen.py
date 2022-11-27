from tkinter import *
import Game_loop

def play_again():
    import Game_loop

def game_over():
    rt = Tk()
    rt.geometry("350x450")
    rt.configure(bg="orange")


    label1 = Label(rt, text="GAME OVER", padx=25, pady=15, bg="orange", fg="black", font=("Arial Bold", 20))
    label1.pack()

    label1.place(relx=0.2, rely=0.4)

    but1 = Button(rt, text="exit", padx=30, pady=12, command=quit, font=("helvetica bold", 12), bg="purple", fg="white")
    but1.pack()
    but1.place(relx=0.4, rely=0.7)

    but2 = Button(rt, text=" play again", padx=30, pady=12, font=("Arial bold", 12), bg="purple", fg="white", command=play_again)
    but2.pack()
    but2.place(relx=0.3, rely=0.2)

    rt.mainloop()